"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models.user import User


class UserSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    photo = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], 
        required=False
    )

    extract = serializers.CharField(max_length=1000, required=False)

    city = serializers.CharField(max_length=250, required=False)

    country = serializers.CharField(max_length=250, required=False)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone = serializers.CharField(validators=[phone_regex], required=False)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)


    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        image = None
        if 'photo' in data:
            image = data['photo']

        if image:
            if image.size > (512 * 1024):
                raise serializers.ValidationError(f"La imagen es demasiado grande, el peso máximo permitido es de 512KB y el tamaño enviado es de {round(image.size / 1024)}KB")

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user
