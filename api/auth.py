from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):
    """ Autenticação customizada dos usuários """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)

        return Response({
            # Como Token.objects.get_or_create retorna tupla devemos especificar o indice do token
            'token': token[0].key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })
