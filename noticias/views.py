from django.shortcuts import render
from .models import Noticias

def noticias(request, ):
    
    noticias = Noticias.objects.all()

    dados = {
        'noticias' : noticias
    }

    return render(request, 'noticias.html', dados)
