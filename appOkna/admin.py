from django.contrib import admin
from .models import CategoryProduct
from .models import Products
from .models import ServiceArticles
from .models import InformationArticles
from .models import Partners

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title','category','price','is_popular')

class ServiceArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')

class InformationArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ServiceArticles, ServiceArticlesAdmin)
admin.site.register(InformationArticles, InformationArticlesAdmin)
admin.site.register(Partners, PartnersAdmin)