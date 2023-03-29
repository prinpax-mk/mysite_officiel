from django.db import models

# Create your models here.

class abonnes(models.Model):
    
    prenom = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=10)  
