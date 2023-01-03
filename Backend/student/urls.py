from django.urls import path
from .views import StudList, StudDetails,deletestudent

urlpatterns=[
     path('studList/',StudList.as_view()),
     path('studDetails/<int:pk>',StudDetails.as_view()),
     
     path('deletestud/<int:pk>',deletestudent.as_view()),
]