from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Сериализатор Приложения
    """

    class Meta:

        model = Application
        fields = ('id', 'name', 'user', 'api_key')
        read_only_fields = ('api_key', 'user')
