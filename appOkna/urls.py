from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.basePage, name='basePage'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product, name='product'),
    url(r'^serviceArticle/(?P<pk>[0-9]+)/$', views.serviceArticle, name='serviceArticle'),
    url(r'^informationArticle/(?P<pk>[0-9]+)/$', views.informationArticle, name='informationArticle'),
]