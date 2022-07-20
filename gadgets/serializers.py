from rest_framework import serializers
from .models import Product, ProductCategory, Tag


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'description', 'price')


class ProductWritableSreailizer(serializers.ModelSerializer):
	class Meta:
		model = Product 
		fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductCategory
		fields = '__all__'