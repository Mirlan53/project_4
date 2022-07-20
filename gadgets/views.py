from rest_framework import generics, serializers
from .models import Product 
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .forms import UserRegisterForm


class ProductList(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_url_kwarg = 'product_id'


class ProductDestroy(generics.DestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_url_kwarg = 'product_id'


def product_list_with_categories(request):
	products = Product.objects.select_related('category').all()
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
			current_site = get_current_site()
			subject = 'Активация'
			message = render_to_string('gadgets/account_activation.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user)
				})
			user.email_user(subject=subject, message=message)
			return redirect('product_list_with_categories')

	context = {
	'reg_form': reg_form
	}

	return render(request, 'gadgets/account_register.html', context)

