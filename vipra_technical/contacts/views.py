from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .models import Contact
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
    print("hello")


@api_view(['GET'])
def home(request):
    api_urls = {
        'List':'/contacts-list/',
        'Add':'/contacts-create/',
        'update':'/contacts-update/<str:pk>/',
        'delete':'/contacts-delete/<str:pk>/'

    }
    return Response(api_urls)

@api_view(['GET'])
def ContacsList(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ContacsCreate(request):
    serializer = ContactSerializer(data = request.data)
    print(serializer)
    if serializer.is_valid():
        print("saved!")
        serializer.save()
        return Response(serializer.data)
    else:
        raise Http404

@api_view(['POST'])
def ContacsUpdate(request, pk):
    contacts = Contact.objects.get(id = pk)
    serializer = ContactSerializer(instance = contacts ,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        raise Http404


@api_view(['DELETE'])
def ContacsDelete(request,pk):
    contacts = Contact.objects.get(id = pk)
    contacts.delete()
    return Response("Contact Deleted")
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})