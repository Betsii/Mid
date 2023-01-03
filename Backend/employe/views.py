from rest_framework import generics
from .serializers import employeSerializer
from .models import employe
# Create your views here.

class Listemploye(generics.ListCreateAPIView):
    queryset=employe.objects.all()
    serializer_class=employeSerializer
    
class deleteemploye(generics.DestroyAPIView):
    queryset=employe.objects.all()
    serializer_class=employeSerializer
    
class updateemploye(generics.UpdateAPIView):
    queryset=employe.objects.all()
    serializer_class=employeSerializer
    
class details(generics.RetrieveUpdateDestroyAPIView):
    queryset=employe.objects.all()
    serializer_class=employeSerializer