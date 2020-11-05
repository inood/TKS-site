from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('documents/', views.documents, name='documents'),
    url(r'^contact/$', views.contactform, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^licenses/$', views.licenses, name='licences'),
    url('about/', views.about, name='about')
]
