from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User


class Noticias(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_noticia = models.CharField(max_length=200)
    texto_noticia = models.TextField()
    categoria_noticia = models.CharField(max_length=200)
    data_noticia = models.DateTimeField(default=datetime.now, blank=True)
    foto_noticia = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)