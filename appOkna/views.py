from django.shortcuts import render, get_object_or_404
from .models import CategoryProduct
from .models import Products
from .models import ServiceArticles
from .models import InformationArticles
from .models import Partners

categoryProduct = CategoryProduct.objects.all()
serviceArticles = ServiceArticles.objects.all()
informationArticles = InformationArticles.objects.all()
partners = Partners.objects.all()

base_context = {
    'categoryProduct': categoryProduct,
    'serviceArticles': serviceArticles,
    'informationArticles': informationArticles,
    'partners': partners
}

def basePage(request):
    return render(request, 'appOkna/base.html', base_context)

def product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'appOkna/product.html', {'product': product})