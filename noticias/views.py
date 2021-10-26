from .models import Noticias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages


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
        noticia = Noticias.objects.order_by('-data_noticia').filter(pessoa=id)

        dados = {
            'noticias' : noticia
        }
        return render(request, 'dashboard.html', dados)
    else:
        messages.error(request, 'Você precisa estar autenticado para visualizar seu dashboard!')
        return redirect('login')

def cria_noticia(request):
    '''Cria uma nova noticia e adiciona no sistema'''
    if request.user.is_authenticated:
        if request.method == 'POST':
            titulo_noticia = request.POST['titulo_noticia']
            texto_noticia = request.POST['texto_noticia']
            previa_noticia = request.POST['previa_noticia']
            categoria_noticia = request.POST['categoria_noticia']
            if 'foto_noticia' in request.FILES:
                foto_noticia = request.FILES['foto_noticia']
            else:
                foto_noticia = ''
            user = get_object_or_404(User, pk=request.user.id)
            noticia = Noticias.objects.create(pessoa=user, titulo_noticia=titulo_noticia, texto_noticia=texto_noticia, previa_noticia=previa_noticia, categoria_noticia=categoria_noticia, 
            foto_noticia=foto_noticia )
            noticia.save()
            return redirect('dashboard')
        else:
            return render(request, 'cria_noticia.html')
    else:
        messages.error(request, 'Você precisa estar autenticado para criar notícias!')
        return redirect('login')

def deleta_noticia(request, noticia_id):
    '''Exclui a noticia selecionada'''
    noticia = get_object_or_404(Noticias, pk=noticia_id)
    noticia.delete()
    return redirect('dashboard')

def edita_noticia(request, noticia_id):
    '''Edita a noticia selecionada'''
    noticia = get_object_or_404(Noticias, pk=noticia_id)
    noticia_a_editar = {'noticia': noticia}
    return render(request, 'edita_noticia.html', noticia_a_editar)

def atualiza_noticia(request):
    '''Atualiza a noticia selecionada'''
    if request.method == 'POST':
        noticia_id = request.POST['noticia_id']
        n = Noticias.objects.get(pk=noticia_id)
        n.titulo_noticia = request.POST['titulo_noticia']
        n.texto_noticia = request.POST['texto_noticia']
        n.previa_noticia = request.POST['previa_noticia']
        n.categoria_noticia = request.POST['categoria_noticia']
        if 'foto_noticia' in request.FILES:
            n.foto_noticia = request.FILES['foto_noticia']
        n.save()
        return redirect('dashboard')
