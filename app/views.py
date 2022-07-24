from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Product
from faker import Faker
import random

def home_page(request):
    return render(request, 'home-page.html')


def product_create_view(request):
    fake = Faker()
    for _ in range(1, 11):
        Product.objects.create(name=fake.name(), description=fake.text(), price=random.randint(1111, 2555), brand=fake.name())
    return JsonResponse('product create completed....')


def product_list_view(request):
    products = Product.objects.all()
    data = []
    for pd in products:
        item = {
            'id': pd.id,
            'title': pd.title,
            'description': pd.description,
            'price': pd.price,
            'brand': pd.brand,
        }
        data.append(item)
    print(data)
    return JsonResponse({'data':data})
