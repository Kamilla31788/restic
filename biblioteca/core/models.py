from core.models import Categoria, Autor, Livro
from datetime import date
# Criando categorias
ficcao = Categoria.objects.create(nome='Ficção')
ciencia = Categoria.objects.create(nome='Ciência')
# Criando autores
asimov = Autor.objects.create(nome='Isaac Asimov')
sagan = Autor.objects.create(nome='Carl Sagan')
# Criando livros
Livro.objects.create(titulo='Fundação', autor=asimov,
categoria=ficcao, publicado_em=date(1951, 6, 1))
Livro.objects.create(titulo='Cosmos', autor=sagan, categoria=ciencia,
publicado_em=date(1980, 10, 1))
# Verificar categorias
print(Categoria.objects.all())

# Verificar autores
print(Autor.objects.all())

# Verificar livros
print(Livro.objects.all())
ficcao_livros = Livro.objects.filter(categoria__nome='Ficção')
for livro in ficcao_livros:
 print(livro.titulo)
fundacao = Livro.objects.get(titulo='Fundação')
fundacao.titulo = 'Fundação - Edição Revisada'
fundacao.save()
cosmos = Livro.objects.get(titulo='Cosmos')
cosmos.delete()
