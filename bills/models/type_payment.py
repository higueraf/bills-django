from django.db.models import CharField, TextField
from common.models.models import CommonData, ErrorMessages
from django.db.models import CharField
from django.utils.text import gettext_lazy as _

class TypePayment(CommonData):
    
    model_name = 'TypePayment'

    name = CharField(
        verbose_name=_('Name'),
        unique=True,
        max_length=255,
        error_messages=ErrorMessages.get_char_field(model=model_name, field='name', is_unique=True)
    )
    description = TextField(
        verbose_name=_('Description'),
        max_length=500,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='description')
        )

    def __str__(self):
        return self.name