from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Livro
from .serializers import LivroSerializer
from .serializers import ColecaoSerializerSerializer
from .custom_permissions import IsColecionador 
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def livro_list_create(request):
    from .models import Livro 
    from .serializers import LivroSerializer
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def livro_detail(request, pk):
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return Response({'detail': 'Livro não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        livro.delete()
        return Response({'message': 'Livro deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)


from .models import Colecao
from .serializers import ColecaoSerializer

from drf_spectacular.utils import extend_schema

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@extend_schema(
    description="Lista todas as coleções e cria uma nova coleção.",
    responses={
        200: ColecaoSerializer,
        201: ColecaoSerializer,
    }
)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # Apenas usuários autenticados podem acessar essas views
def ColecaoListCreate(request):
    # Listando as coleções
    if request.method == 'GET':
        colecoes = Colecao.objects.all()
        serializer = ColecaoSerializer(colecoes, many=True)
        return Response(serializer.data)

    # Criando uma nova coleção
    elif request.method == 'POST':
        # Garantir que o usuário autenticado seja o colecionador
        request.data['colecionador'] = request.user.id
        serializer = ColecaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated]) 
def ColecaoDetail(request, pk):
    try:
        colecao = Colecao.objects.get(pk=pk)
    except Colecao.DoesNotExist:
        return Response({'detail': 'Coleção não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    # Apenas o colecionador pode editar ou excluir a coleção
    if colecao.colecionador != request.user:
        return Response({'detail': 'Você não tem permissão para modificar essa coleção.'},
                        status=status.HTTP_403_FORBIDDEN)

    # Visualizando a coleção (qualquer usuário pode)
    if request.method == 'GET':
        serializer = ColecaoSerializer(colecao)
        return Response(serializer.data)

    # Editando a coleção (somente o colecionador pode)
    elif request.method == 'PUT':
        serializer = ColecaoSerializer(colecao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deletando a coleção (somente o colecionador pode)
    elif request.method == 'DELETE':
        colecao.delete()
        return Response({'message': 'Coleção deletada com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    

