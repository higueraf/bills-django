from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import UniqueValidator

# Models
from users.models.user import User

class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')
        self.context['user'] = user
        return data

    def create(self, data):
        refresh = RefreshToken.for_user(self.context['user'])
        return self.context['user'], str(refresh.access_token), str(refresh)
