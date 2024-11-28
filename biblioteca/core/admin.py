from django.contrib import admin

from .models import Categoria, Autor,Livro

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Livro)


