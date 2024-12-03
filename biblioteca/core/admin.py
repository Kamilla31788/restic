from django.contrib import admin

from .models import Categoria, Autor,Livro

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Livro)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass



