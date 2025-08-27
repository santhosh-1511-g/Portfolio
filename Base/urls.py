from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # for homepage
    path('contact/', views.contact, name='contact'),
]