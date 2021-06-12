from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name = 'contacts-home'),
    path('contact/<int:pk>/', views.DetailView, name='contact-details'),

]