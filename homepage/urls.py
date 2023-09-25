from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage_home, name='homepage-home'),
    path('about/', views.homepage_about, name='homepage-about'),
]
