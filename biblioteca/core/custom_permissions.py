from rest_framework import permissions

class IsColecionador(permissions.BasePermission):
    """
    Permissão personalizada para garantir que apenas o colecionador
    possa modificar sua coleção.
    """

    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário é o colecionador da coleção
        if request.method in permissions.SAFE_METHODS:
            return True  # Permite acesso para métodos de leitura (GET)
        
        # Para métodos de escrita (PUT, DELETE), apenas o colecionador pode modificar
        return obj.colecionador == request.user
