from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product


# Create your views here.
def homepage(request):
    return HttpResponse('hello')


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'

    def get_queryset(self):
        return Product.objects.all()
