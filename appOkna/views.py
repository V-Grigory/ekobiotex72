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
    base_context['product'] = product
    return render(request, 'appOkna/product.html', base_context)

def serviceArticle(request, pk):
    serviceArticle = get_object_or_404(ServiceArticles, pk=pk)
    base_context['serviceArticle'] = serviceArticle
    return render(request, 'appOkna/serviceArticle.html', base_context)

def informationArticle(request, pk):
    informationArticle = get_object_or_404(InformationArticles, pk=pk)
    base_context['informationArticle'] = informationArticle
    return render(request, 'appOkna/informationArticle.html', base_context)