from django.urls import path
from gadgets.views import ProductList, ProductDetails, ProductDestroy, product_list_with_categories

urlpatterns = [
    path('products', ProductList.as_view(), name='products'),
    path('products/<int:product_id>/delete', ProductDetails.as_view(), name='product_details'),
    path('products/<int:product_id>', ProductDestroy.as_view(), name='products_destroy'), 
    path('product_list_with_categories', product_list_with_categories, name='product_list_with_categories'),

]
