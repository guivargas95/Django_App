from django.shortcuts import render, get_object_or_404
from .models import Pizza

def index(request):
    return render(request, 'index.html')

def pizza(request):
    
    pizzas = Pizza.objects.all()

    dados = {
        'pizzas' : pizzas
    }

    return render(request, 'pizza.html', dados)
