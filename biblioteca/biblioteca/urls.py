"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path('livros/', views.livro_list_create, name='livros-list-create'),
    path('livros/<int:pk>/', views.livro_detail, name='livro-detail'),
    path('colecao/', views.ColecaoListCreate, name='colecao_list_create'),
    path('colecao/<int:pk>/', views.ColecaoDetail, name='colecao_detail'),
    path('colecao/', views.ColecaoListCreate, name='colecao_list_create'),
    path('colecao/<int:pk>/', views.ColecaoDetail, name='colecao_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Documentação da API
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Endpoint para gerar o schema OpenAPI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),  # Visualizar a documentação interativa 

]
