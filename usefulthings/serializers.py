from rest_framework.serializers import ModelSerializer

from usefulthings.models import Wont


class WontSerializer(ModelSerializer):
    """Класс сериализатора для модели привычки"""

    class Meta:
        model = Wont
        fields = "__all__"
        read_only_fields = ["id", "owner"]

    def validate(self, attrs):
        """Функция валидации полей модели привычки"""
        wont = Wont(**attrs)
        wont.clean()
        return attrs
