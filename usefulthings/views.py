from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from usefulthings.models import Wont
from usefulthings.serializers import WontSerializer
from users.permissions import IsOwner

from .paginators import MyPagination


class WontCreateApiView(CreateAPIView):
    """Класс контроллера для создания привычки"""

    queryset = Wont.objects.all()
    serializer_class = WontSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serialazer):
        """метод автоматического сохранения пользователя в поле владельца"""
        wont = serialazer.save()
        wont.owner = self.request.user
        wont.save()


class WontListApiView(ListAPIView):
    """Класс контроллера для вывода списка привычек"""

    queryset = Wont.objects.all()
    serializer_class = WontSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        """метод отображения привычек заданного пользователя"""
        return Wont.objects.filter(owner=self.request.user)


class WontRetrieveApiView(RetrieveAPIView):
    """Класс контроллера для вывода экземпляра привычки"""

    queryset = Wont.objects.all()
    serializer_class = WontSerializer
    permission_classes = (IsOwner,)


class WontUpdateApiView(UpdateAPIView):
    """Класс контроллера для изменения экземпляра привычки"""

    queryset = Wont.objects.all()
    serializer_class = WontSerializer
    permission_classes = (IsOwner,)


class WontDestroyApiView(DestroyAPIView):
    """Класс контроллера для удаления экземпляра привычки"""

    queryset = Wont.objects.all()
    serializer_class = WontSerializer
    permission_classes = (IsOwner,)


class PublishedWontListView(ListAPIView):
    """Класс контроллера для списка публичных привычек"""

    queryset = Wont.objects.filter(is_published=True)
    serializer_class = WontSerializer
    permission_classes = [
        AllowAny
    ]  # Любой пользователь может видеть публичные привычки
