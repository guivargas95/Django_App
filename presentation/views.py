from django.shortcuts import render, get_object_or_404
#from .model import Receita

def index(request):
    return render(request, 'index.html')

def pizza(request):
    return render(request, 'pizza.html')
