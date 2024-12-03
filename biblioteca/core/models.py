from django.db import models
from django.conf import settings  
from django.contrib.auth.models import AbstractUser


class Categoria(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Autor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Livro(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    autor = models.ForeignKey(Autor, related_name="livros", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name="livros", on_delete=models.CASCADE)
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo


class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    livros = models.ManyToManyField(Livro, related_name="colecoes")
    colecionador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="colecoes")

    def __str__(self):
        return f"{self.nome} - {self.colecionador.username}"


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)  # Exemplo de campo extra

