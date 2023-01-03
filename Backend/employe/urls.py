from django.urls import path
from .views import Listemploye, deleteemploye, updateemploye,details

urlpatterns = [
    path('Listemploye/',Listemploye.as_view()),
    path('deletemploye/<int:pk>',deleteemploye.as_view()),
    path('updateemploye/<int:pk>',updateemploye.as_view()),
    path('details/<int:pk>',details.as_view())
]
