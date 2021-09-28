from django.db import models
from datetime import date, datetime

class Pizza(models.Model):
    nome_pizza = models.CharField(max_length=200)
    ingredientes = models.TextField()
    categoria = models.CharField(max_length=100)
    data_cadastro = models.DateField(default=datetime.now, blank=True)
    
