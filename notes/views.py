

from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from server.settings import AUTH_USER_MODEL
from rest_framework.decorators import api_view

# Create your views here.
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserNotes(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = NotesSerializer
    def get_queryset(self):
        User = self.request.user   
        queryset = Notes.objects.filter(user = self.request.user)
        return queryset
    
class EditNotes(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = NotesSerializer

    queryset = Notes.objects.all()
    
class AppendNote(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = NotesSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        note = Notes.objects.get(id=pk)
        print(self.request.data.get('content'))
        note.content += self.request.data.get('content')
        note.save()
        
        
        # print(pk)    
