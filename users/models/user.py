from django.db.models import EmailField, DateTimeField, ImageField, CharField, ForeignKey, PROTECT
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

from common.models.models import CommonData, ErrorMessages
from companies.models.company import Company


class User(AbstractUser):
    
    model_name = 'User'

    email = EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    modified = DateTimeField(auto_now=True)
    photo = ImageField(null=True, upload_to='users')
    extract = RichTextField(null=True)
    phone = CharField(null=True, max_length=15)
    city = CharField(null=True, max_length=255)
    country = CharField(null=True, max_length=255)
    company = ForeignKey(
        to=Company,
        on_delete=PROTECT,
        null=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='company_id')
    )