from django.contrib import admin
from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.index,name='home'),
    path('index', views.index,name='home'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('contactus', views.contactus,name='contact'),
    path('contact', views.contactus,name='contact'),
]