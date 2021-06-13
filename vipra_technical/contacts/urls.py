from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name = 'contacts-home'),
    path('contacts-list/', views.ContacsList, name='contacts-list'),
    path('contacts-detail/<str:pk>/', views.ContacsDetail, name='contacts-detail'),
    path('contacts-create/', views.ContacsCreate, name='contacts-create'),
    path('contacts-update/<str:pk>/', views.ContacsUpdate, name='contacts-update'),
]