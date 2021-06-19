from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('contacts-list/', views.ContacsList, name='contacts-list'),
    path('contacts-create/', views.ContacsCreate, name='contacts-create'),
    path('contacts-update/<str:pk>/', views.ContacsUpdate, name='contacts-update'),
    path('contacts-delete/<str:pk>/', views.ContacsDelete, name='contacts-delete'),
    path('API/', views.ContactList.as_view()),
    path('API/<str:pk>/', views.ContactActions.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)