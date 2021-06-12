from django.urls import path
from . import views
from .views import ContactCreateView, ContactUpdateView, ContactDeleteView


urlpatterns = [
    path('',views.home, name = 'contacts-home'),
    path('contact/<int:pk>/', views.DetailView, name='contact-details'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
]