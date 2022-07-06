from django.urls import path
from gadgets.views import ProductList, ProductDetail, ProductDestroy

urlpatterns = [
    path('products', ProductList.as_view(), name='products'),
    path('products/<int:product_id>/delete', ProductDetail.as_view(), name='product_detail'),
    path('products/<int:product_id>', ProductDestroy.as_view(), name='products_destroy'), 
]
