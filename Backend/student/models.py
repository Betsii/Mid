from django.db import models

# Create your models here.
class Student(models.Model):
    studentName=models.CharField(max_length=50)
    

    def str(self):
        return self.studentName