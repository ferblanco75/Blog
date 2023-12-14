from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        #si el pedido es get o post. cualquiera lo puede hacer(crear u obtener coments)
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            #ahora obtengo la info del comentario
            comment = Comment.objects.get(pk=id_comment)
            # ahora obtengo el id del usuario que hace la peticion

            id_user = request.user.pk
            id_user_comment = comment.user_id
            if id_user == id_user_comment:
                return True

            return False