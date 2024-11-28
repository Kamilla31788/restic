from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Colecao, Livro

class ColecaoTests(TestCase):
    def setUp(self):
        # Criando um usuário
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Autenticando o usuário
        
        # Criando um livro para associar à coleção
        self.livro = Livro.objects.create(
            titulo="Livro de Teste",
            autor="Autor de Teste",
            categoria="Categoria de Teste",
            publicado_em="2024-01-01"
        )

    def test_create_colecao(self):
        # Dados para criar a coleção
        data = {
            "nome": "Minha Coleção",
            "livros": [self.livro.id],
        }

        response = self.client.post('/colecao/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 1)
        colecao = Colec

