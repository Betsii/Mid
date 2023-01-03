from django.urls import path
from .views import ListTeachers, deleteTeachers, updateTeachers,details

urlpatterns = [
    path('ListTeach/',ListTeachers.as_view()),
    path('deletTeach/<int:pk>',deleteTeachers.as_view()),
    path('updateTeach/<int:pk>',updateTeachers.as_view()),
    path('details/<int:pk>',details.as_view())
]
