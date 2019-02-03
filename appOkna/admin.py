from django.contrib import admin
from .models import Mainpage
from .models import CategoryProduct
from .models import Params
from .models import Products
from .models import ServiceArticles
from .models import InformationArticles
from .models import Partners

# Mainpage
class MainpageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'keywords')

admin.site.register(Mainpage, MainpageAdmin)

# CategoryProduct
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')

admin.site.register(CategoryProduct, CategoryProductAdmin)

# Products (with Params)
class Params(admin.StackedInline):
    model = Params
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title','category','price','is_popular')
    inlines = [Params]

admin.site.register(Products, ProductsAdmin)

# ServiceArticles
class ServiceArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')

admin.site.register(ServiceArticles, ServiceArticlesAdmin)

# InformationArticles
class InformationArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

admin.site.register(InformationArticles, InformationArticlesAdmin)

# Partners
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

admin.site.register(Partners, PartnersAdmin)
