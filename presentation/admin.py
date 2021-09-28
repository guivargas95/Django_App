from django.contrib import admin
from .models import Pizza

class ListandoPizzas(admin.ModelAdmin):
    list_display = ('id', 'nome_pizza', 'categoria')
    list_display_links = ('id', 'nome_pizza')
    search_fields = ('nome_pizza',)
    list_filter = ('categoria',)


admin.site.register(Pizza, ListandoPizzas)
