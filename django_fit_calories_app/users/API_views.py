from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.permissions import IsOwnerOrReadOnly
from .models import CustomUser, Weighing

from .serializers import ProfileSerializer, WeighingSerializer


class AllProfileAPIViewSet(viewsets.ModelViewSet):
    """Список всех пользователей"""

    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, )


class ProfileAPIViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """Профиль пользователя"""

    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.id
        user_profile = CustomUser.objects.filter(id=user)
        return user_profile


class WeighingAPIViewSet(viewsets.ModelViewSet):
    """Взвешивание"""

    serializer_class = WeighingSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.id
        return Weighing.objects.filter(user=user).order_by('weighing_date')
