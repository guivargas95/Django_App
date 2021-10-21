from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('<int:noticia_id>', views.noticia, name='noticia'),
    #path('buscar', buscar, name='buscar'),
    #path('cria/receita', cria_receita, name='cria_receita'),
    #path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    #path('edita/<int:receita_id>', edita_receita, name='edita_receita'),
    #path('atualiza_receita', atualiza_receita, name='atualiza_receita'),
    
        
]