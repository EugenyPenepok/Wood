from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from wood.models import *


def get_values(_request):
    return render(_request, 'index.html')


def get_category(_request):
    categories = Category.objects.all()
    context = {"category": categories}
    return render(_request, "category.html", context)


def get_category_content(_request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category_id=category_id)
    context = {"product": products, "category": category}
    return render(_request, "list.html", context)


def get_product_add(_request, category_id):
    covers = Coating.objects.all()
    materials = Material.objects.all()
    sizes = Size.objects.all()
    context = {"category_id": category_id, "covers": covers,"materials":materials,"sizes":sizes}
    return render(_request, 'addproduct.html', context)
