
from common.models.models import CommonData, ErrorMessages
from common.models import Municipality
from django.db.models import (PROTECT, CharField, ForeignKey)

from django.utils.text import gettext_lazy as _

class Parish(CommonData):
    model_name = 'Parish'

    name = CharField(
        verbose_name=_('Name'),
        unique=True,
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='nombre', is_unique=True)
    )
    detail = CharField(
        verbose_name=_('Detail'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='detalle')
    )

    municipality: Municipality = ForeignKey(
        verbose_name=_('Municipality'),
        to=Municipality,
        on_delete=PROTECT,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(model=model_name, field='municipality_id')
    )