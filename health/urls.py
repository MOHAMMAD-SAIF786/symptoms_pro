from django.urls import path
from . import views  # this imports your views.py file

urlpatterns = [
    path('', views.home, name='home'),  # example URL
    path('contact/', views.contact, name='contact'),  # example URL
    path('health-chatbot/', views.health_chatbot, name='health_chatbot'),
]
