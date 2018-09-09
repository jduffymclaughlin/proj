
from django.urls import path

from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'services', views.services, name='services'), 
    path(r'about_me', views.about_me, name='about_me'),
    path(r'contact', views.contact, name='contact'),
    path(r'book_now', views.book_now, name='book_now'),
]