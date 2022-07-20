from common.models.models import CommonData, ErrorMessages
from django.db.models import (PROTECT, CharField, ForeignKey)

from django.utils.text import gettext_lazy as _
from common.models import Country

class State(CommonData):
    model_name = 'State'

    name = CharField(
        verbose_name=_('Name'),
        unique=False,
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name,
            field='name'
        )
    )
    detail = CharField(
        verbose_name=_('Detail'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, 
            field='detalle'
        )
    )
    country = ForeignKey(
        verbose_name=_('Country'),
        to=Country,
        on_delete=PROTECT,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, 
            field='country_id'
        )
    )

    def __str__(self):
        return self.name