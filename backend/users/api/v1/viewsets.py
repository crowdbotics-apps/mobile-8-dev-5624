from rest_framework import authentication
from users.models import Hgjkhglkj
from .serializers import HgjkhglkjSerializer
from rest_framework import viewsets


class HgjkhglkjViewSet(viewsets.ModelViewSet):
    serializer_class = HgjkhglkjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hgjkhglkj.objects.all()
