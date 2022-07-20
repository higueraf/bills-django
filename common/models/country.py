from django.db import models
from common.models.models import CommonData, ErrorMessages
from django.db.models import CharField
from django.utils.text import gettext_lazy as _

class Country(CommonData):
    model_name = 'Country'

    name = CharField(
        verbose_name=_('Name'),
        unique=True,
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='name', is_unique=True
        )
    )
    name_sp = CharField(
        verbose_name=_('Name Sp'), 
        max_length=255,
        blank=True,
        null=True,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='name_sp'
        )
    )
    nam = CharField(
        verbose_name=_('Nam'), 
        max_length=255,
        blank=True,
        null=True,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, 
            field='nam'
        )
    )
    iso2 = CharField(
        verbose_name=_('iso2'), 
        max_length=10,
        blank=True,
        null=True,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, 
            field='iso2'
        )
    )
    iso3 = CharField(
        verbose_name=_('iso3'), 
        max_length=10,
        blank=True,
        null=True,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, 
            field='iso3'
        )
    )
    phone_code = CharField(
        verbose_name=_('Phone code'),
        max_length=10,
        blank=True,
        null=True,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, 
            field='phone_code'
        )
    )

    def __str__(self):
        return self.name_sp