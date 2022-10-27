from django.urls import path
from .views import (
    home_page,
    product_view,
    product_create_view,
    product_update_view
)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/update/', product_update_view, name='product-update'),
    path('product/list/', product_view, name='product_view'),
]