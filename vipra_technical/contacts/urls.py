from django.urls import path
from . import views
from .views import ContactCreateView


urlpatterns = [
    path('',views.home, name = 'contacts-home'),
    path('contact/<int:pk>/', views.DetailView, name='contact-details'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
]