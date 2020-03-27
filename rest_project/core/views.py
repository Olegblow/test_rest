from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Application
from .permissions import IsOwnerOrApiKey
from .serializers import ApplicationSerializer
from .services import generate_api_key


class ApplicationSet(CreateAPIView):
    """Вьюха Создания Приложения."""

    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        api_key = generate_api_key(self.request.user)
        serializer.save(
            user=self.request.user,
            api_key=api_key
        )


class UpdateApikey(UpdateAPIView):
    """вьюха апдейтит API KEY приложения."""

    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated, IsOwnerOrApiKey]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_update(self, serializer):
        api_key = generate_api_key(self.request.user)
        serializer.save(api_key=api_key)


class Test(RetrieveAPIView):
    """Вьюха возвращает данные приложения по API KEY"""

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = 'api_key'
