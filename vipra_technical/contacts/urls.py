from django.urls import path
from . import views

urlpatterns = [
    path('contacts-list/', views.ContacsList, name='contacts-list'),
    path('contacts-create/', views.ContacsCreate, name='contacts-create'),
    path('contacts-update/<str:pk>/', views.ContacsUpdate, name='contacts-update'),
    path('contacts-delete/<str:pk>/', views.ContacsDelete, name='contacts-delete'),
]