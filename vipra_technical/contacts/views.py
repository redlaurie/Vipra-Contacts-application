from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .models import Contact
from rest_framework import status
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer

class ContactList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactActions(APIView):
    print("hello")

    def put(self,request,pk,format=None):
        contact = Contact.objects.get(id = pk)
        serializer = ContactSerializer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contact = Contact.objects.get(id = pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
