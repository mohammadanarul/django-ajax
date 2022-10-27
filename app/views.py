from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Product
from faker import Faker
import random
from .forms import ProductForm

def home_page(request):
    return render(request, 'home-page.html')

def product_create_view(request):
    # request should be ajax and method should be POST.
    if request.is_ajax():
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)


def product_update_view(request):
    # request should be ajax and method should be POST.
    if request.is_ajax():
        pk = request.GET.get('id')
        product = Product.objects.get(pk=pk)
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"updated": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)

# class UpdateCrudUser(View):
#     def get(self, request):
#         pk = request.GET.get('id', None)
#         CrudUser.objects.get(id=pk)

#         obj = CrudUser.objects.get(id=id1)
#         obj.name = name1
#         obj.address = address1
#         obj.age = age1
#         obj.save()

#         user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

#         data = {
#             'user': user
#         }
#         return JsonResponse(data)

'''
def product_create_view(request):
    fake = Faker()
    for _ in range(1, 11):
        Product.objects.create(title=fake.name(), description=fake.text(), price=random.randint(1111, 2555), brand=fake.name())
    return JsonResponse({'success': 'product create completed....'})
'''

def product_view(request):
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
