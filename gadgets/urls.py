from django.urls import path
from gadgets.views import ProductList, ProductDetail, ProductDestroy, product_list_with_categories, account_register, account_activation

urlpatterns = [
    path('products', ProductList.as_view(), name='products'),
    path('products/<int:product_id>/delete', ProductDetail.as_view(), name='product_detail'),
    path('products/<int:product_id>', ProductDestroy.as_view(), name='products_destroy'), 
    path('product_list_with_categories', product_list_with_categories, name='product_list_with_categories'),
    path('account_register', account_register, name='account_register'),
    path('account_activation', account_activation, name='account_activation'),
]
