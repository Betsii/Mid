from rest_framework import generics
from .serializers import TeachersSerializer
from .models import Teachers
# Create your views here.

class ListTeachers(generics.ListCreateAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeachersSerializer
    
class deleteTeachers(generics.DestroyAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeachersSerializer
    
class updateTeachers(generics.UpdateAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeachersSerializer
    
class details(generics.RetrieveUpdateDestroyAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeachersSerializer