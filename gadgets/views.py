from rest_framework import generics, serializers
from .models import Product 
from .serializers import ProductSerializer
from django.shortcuts import render


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