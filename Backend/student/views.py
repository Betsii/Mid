

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student
# Create your views here.

class StudList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class deletestudent(generics.DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer