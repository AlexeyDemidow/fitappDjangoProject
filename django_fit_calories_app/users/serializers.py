from rest_framework import serializers

from .models import CustomUser, Weighing


# Сериалайзер профиля пользователя
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories')


class WeighingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weighing
        fields = ('id', 'weighing_date', 'weight_value', 'user', )
