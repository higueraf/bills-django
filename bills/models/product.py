from django.db.models import CharField, DecimalField, TextField, ForeignKey, PROTECT
from django.utils.text import gettext_lazy as _

from common.models.models import CommonData, ErrorMessages
from common.models.tax import Tax
from companies.models.company import Company
from users.models.user import User


class Product(CommonData):
    model_name = 'Product'
    name = CharField(
        verbose_name=_('Name'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='name'
        )
    )
    description = TextField(
        verbose_name=_('Description'),
        max_length=500,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='description')
    )
    tax = ForeignKey(
        to=Tax,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(model=model_name, field='tax_id')
    )
    unit_price = DecimalField(
        verbose_name=_('Percent'),
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(model=model_name, field='percent', is_null=True, is_blank=True)
    )
    company = ForeignKey(
        to=Company,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='company_id'
        )
    )
    user = ForeignKey(
        to=User,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='user_id'
        )
    )
    