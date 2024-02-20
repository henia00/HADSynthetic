from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('models/', views.models, name='models'),
    path('tools/', views.tools, name='tools'),
    path('papers/', views.papers, name='papers'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
