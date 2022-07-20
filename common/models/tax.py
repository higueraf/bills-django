from django.db.models import DecimalField, CharField
from common.models.models import CommonData, ErrorMessages
from django.db.models import CharField
from django.utils.text import gettext_lazy as _

class Tax(CommonData):
    
    model_name = 'Tax'

    name = CharField(
        verbose_name=_('Name'),
        unique=True,
        max_length=255,
        error_messages=ErrorMessages.get_char_field(model=model_name, field='name', is_unique=True)
    )
    percent = DecimalField(
        verbose_name=_('Percent'),
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(model=model_name, field='percent', is_null=True, is_blank=True)
    )

    def __str__(self):
        return self.name_sp