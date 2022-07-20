from django.db import models
from common.models.models import CommonData, ErrorMessages
from common.models import State
from django.db.models import (PROTECT, CharField,ForeignKey)

from django.utils.text import gettext_lazy as _

class Municipality(CommonData):
    model_name = 'Municipality'

    name = CharField(
        verbose_name=_('Name'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='nombre')
        )

    detail = CharField(
        verbose_name=_('Detail'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='detalle')
        )

    state = ForeignKey(
        verbose_name=_('State'),
        to=State,
        on_delete=PROTECT,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, 
            field='state_id'
        )
    )