from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# localhost : 8000/blog 
urlpatterns = [
    path('', views.blog, name= "blog"),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]