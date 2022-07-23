from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .forms import UserRegisterForm
from .models import Product, ProductCategory, Tag, Manufacturer
from .serializers import ProductSerializer, ProductWritableSerializer, ProductCategorySerializers
from django.contrib.auth import login
from django.contrib.auth.models import User


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWritableSerializer



class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWritableSerializer

   

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWritableSerializer



class CategoryListCreate(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializers



def product_list_with_categories(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'gadgets/product_list_with_categories.html', context)



def account_register(request):
    reg_form = UserRegisterForm()
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Активация'
            message = render_to_string('gadgets/account_activation.html',
            {
                'user':user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            user.email_user(subject=subject, message=message, )
            
            return redirect('product_list_with_categories')
    
    context ={
        'reg_form': reg_form
    }
    return render(request, 'gadgets/account_register.html',context)


def account_activation(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('product_list_with_categories')

    else:
        return render(request, 'gadgets/activation_failed.html')
        
    return render(request, 'gadgets/product_list_with_categories.html')


