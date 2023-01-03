from django.db import models

# Create your models here.
class employe(models.Model):
    empName=models.CharField(max_length=30)
   
    
    def str(self):
        return self.empName
    