from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from noticias.models import Noticias

def cadastro(request):
    '''Cadastra uma nova pessoa no sistema'''
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            messages.error(request, 'O usuario não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario já foi cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuario já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso! test')
        return redirect('login')
    else:
        return render(request, 'usuarios\cadastro.html')

def login(request):
    '''Realiza o login de uma pessoa no sistema'''
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            print(nome)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')

            
        

    return render(request, 'usuarios\login.html')

def logout(request):
    '''Realiza o logout de uma pessoa no sistema'''
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    '''Mostra o dashboard da pessoa logada no sistema'''
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas' : receitas
        }
        return render(request, 'usuarios\dashboard.html', dados)
    else:
        return redirect('index')

