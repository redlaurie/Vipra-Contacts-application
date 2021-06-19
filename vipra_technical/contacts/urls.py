from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('API/', views.ContactList.as_view()),
    path('API/<str:pk>/', views.ContactActions.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)