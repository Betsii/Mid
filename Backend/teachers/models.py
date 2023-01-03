from django.db import models

# Create your models here.
class Teachers(models.Model):
    fname=models.CharField(max_length=30)
   
    def str(self):
        return self.fname
    