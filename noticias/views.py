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

def dashboard(request):
    '''Mostra o dashboard da pessoa logada no sistema'''
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Noticias.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas' : receitas
        }
        return render(request, 'usuarios\dashboard.html', dados)
    else:
        return redirect('index')