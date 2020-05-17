from django.db import models

class Entery(models.Model):
    id=models.CharField(max_length=10, primary_key=True)
    data1=models.CharField(max_length=50)
    data2=models.CharField(max_length=50)

    def __str__(self):
        return self.data1

# Create your models here.
