from .models import Noticias
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User


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
        return redirect('login')

def cria_noticia(request):
    '''Cria uma nova noticia e adiciona no sistema'''
    if request.method == 'POST':
        titulo_noticia = request.POST['titulo_noticia']
        texto_noticia = request.POST['texto_noticia']
        previa_noticia = request.POST['previa_noticia']
        categoria_noticia = request.POST['categoria_noticia']
        foto_noticia = request.FILES['foto_noticia']
        user = get_object_or_404(User, pk=request.user.id)
        noticia = Noticias.objects.create(pessoa=user, titulo_noticia=titulo_noticia, texto_noticia=texto_noticia, previa_noticia=previa_noticia, categoria_noticia=categoria_noticia, 
         foto_noticia=foto_noticia )
        noticia.save()
        return redirect('dashboard')
    else:
        return render(request, 'cria_noticia.html')

def deleta_noticia(request, noticia_id):
    '''Exclui a noticia selecionada'''
    noticia = get_object_or_404(Noticias, pk=noticia_id)
    noticia.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    '''Edita a receita selecionada'''
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita': receita}
    return render(request, 'receitas/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    '''Atualiza a receita selecionada'''
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')
