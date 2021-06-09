from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.serveices, name='services')
]
