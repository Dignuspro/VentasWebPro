from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_venta/', views.add_venta, name='add_venta'),
]
