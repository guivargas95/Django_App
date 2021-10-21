from .models import Noticias
from django.shortcuts import render, redirect, get_object_or_404


def noticias(request, ):
    '''Exibe a página de todas as noticias cadastradas'''    
    noticias = Noticias.objects.all()

    dados = {
        'noticias' : noticias
    }

    return render(request, 'noticias.html', dados)


def noticia(request, noticia_id):
    '''Exibe a página da noticia selecionada'''
    noticia = get_object_or_404(Noticias, pk=noticia_id)

    noticia_a_exibir = {
        'noticia' : noticia
    }
    return render(request, 'noticia.html', noticia_a_exibir)