from django.db.models import DecimalField, ForeignKey, PROTECT
from django.utils.text import gettext_lazy as _

from common.models.models import CommonData, ErrorMessages
from bills.models.type_payment import TypePayment
from companies.models.client import Client
from companies.models.company import Company
from users.models.user import User


class Bill(CommonData):

    model_name = 'Bill'
    
    subtotal = DecimalField(
        verbose_name=_('Subtotal'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='subtotal',
            is_null=True,
            is_blank=True
        )
    )
    tax = DecimalField(
        verbose_name=_('Tax'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='tax',
            is_null=True,
            is_blank=True
        )
    )
    total = DecimalField(
        verbose_name=_('Total'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='total',
            is_null=True,
            is_blank=True
        )
    )
    client = ForeignKey(
        to=Client,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='client_id')
    )
    company = ForeignKey(
        to=Company,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='company_id')
    )
    type_payment = ForeignKey(
        to=TypePayment,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='type_payment_id')
    )
    user = ForeignKey(
        to=User,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='user_id')
    )
    