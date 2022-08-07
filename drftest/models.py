from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    mbti = models.CharField(max_length=100)


class Coordination (models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE,related_name="clients")
    top = models.CharField(max_length=100)
    bottom = models.CharField(max_length=100)
    shoes = models.CharField(max_length=100)
    
