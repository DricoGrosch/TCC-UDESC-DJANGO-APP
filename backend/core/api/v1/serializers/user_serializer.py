from django.contrib.auth import get_user_model
from rest_framework import fields
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    token = fields.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def get_token(self, instance):
        _token = Token.objects.get(user=instance)
        return _token.key