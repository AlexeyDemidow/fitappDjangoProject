from rest_framework import serializers

from .models import CustomUser, Weighing


class ProfileSerializer(serializers.ModelSerializer):
    """Сериалайзер профиля пользователя"""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories')


class WeighingSerializer(serializers.ModelSerializer):
    """Сериалайзер взвешивания"""

    class Meta:
        model = Weighing
        fields = ('id', 'weighing_date', 'weight_value', 'user', )
