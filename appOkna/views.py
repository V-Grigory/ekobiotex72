# from django.core.exceptions import *
from django.shortcuts import render, get_object_or_404
from .models import CategoryProduct
from .models import Products
from .models import ServiceArticles
from .models import InformationArticles
from .models import Partners
from .models import Mainpage

categoryProduct = CategoryProduct.objects.all()
serviceArticles = ServiceArticles.objects.all()
informationArticles = InformationArticles.objects.all()
partners = Partners.objects.all()
mainPageParams = Mainpage.objects.get(pk=1)

base_context = {
    'categoryProduct': categoryProduct,
    'serviceArticles': serviceArticles,
    'informationArticles': informationArticles,
    'partners': partners,
    'seo': {
        'title': mainPageParams.title,
        'description': mainPageParams.description,
        'keywords': mainPageParams.keywords
    }
}
# breadcrumbs

def basePage(request):
    return render(request, 'appOkna/base.html', base_context)


def categoryProducts(request, categorySlug):

    categoryProducts = CategoryProduct.objects.get(slug=categorySlug)
    base_context['categoryProducts'] = categoryProducts

    return render(request, 'appOkna/categoryProducts.html', base_context)


def product(request, category, slug):

    # product = get_object_or_404(Products, pk=pk)
    product = get_object_or_404(Products, slug=slug)

    base_context['product'] = product
    base_context['seo']['title'] = product.pagetitle
    base_context['seo']['description'] = product.description
    base_context['seo']['keywords'] = product.keywords

    return render(request, 'appOkna/product.html', base_context)


def service(request):
    return render(request, 'appOkna/service.html', base_context)


def serviceArticle(request, slug):

    serviceArticle = get_object_or_404(ServiceArticles, slug=slug)

    base_context['serviceArticle'] = serviceArticle
    base_context['seo']['title'] = serviceArticle.pagetitle
    base_context['seo']['description'] = serviceArticle.description
    base_context['seo']['keywords'] = serviceArticle.keywords

    return render(request, 'appOkna/serviceArticle.html', base_context)


def information(request):
    return render(request, 'appOkna/information.html', base_context)


def informationArticle(request, slug):

    informationArticle = get_object_or_404(InformationArticles, slug=slug)

    base_context['informationArticle'] = informationArticle
    base_context['seo']['title'] = informationArticle.pagetitle
    base_context['seo']['description'] = informationArticle.description
    base_context['seo']['keywords'] = informationArticle.keywords

    return render(request, 'appOkna/informationArticle.html', base_context)