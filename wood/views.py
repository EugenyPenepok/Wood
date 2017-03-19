from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from wood.models import Category


def get_values(_request):
    return render(_request, 'index.html')


def get_category(_request):
    categories = Category.objects.all()
    context = {"category": categories}
    return render(_request, "category.html", context)
