from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_values(_request):
    return render(_request, 'index.html')
