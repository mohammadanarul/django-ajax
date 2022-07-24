from django.urls import path
from .views import (
    home_page,
    product_list_view,
)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('product/list/', product_list_view, name='product_list_view'),
]