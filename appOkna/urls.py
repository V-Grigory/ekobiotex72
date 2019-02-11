from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.basePage, name='basePage'),

    url(r'^service/$', views.service, name='service'),
    url(r'^service/(?P<slug>[\w-]+)/$', views.serviceArticle, name='serviceArticle'),

    url(r'^information/$', views.information, name='information'),
    url(r'^information/(?P<slug>[\w-]+)/$', views.informationArticle, name='informationArticle'),

    url(r'^(?P<categorySlug>[\w-]+)/$', views.categoryProducts, name='categoryProducts'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', views.product, name='product'),
]