from django.db.models import DecimalField, ForeignKey, PROTECT
from django.utils.text import gettext_lazy as _
from common.models.models import CommonData, ErrorMessages
from common.models.tax import Tax
from bills.models import Bill, Product
from users.models.user import User


class BillDetail(CommonData):

    model_name = 'BillDetail'

    bill = ForeignKey(
        to=Bill,
        on_delete=PROTECT,
        related_name='bill_details',
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='bill_id'
        )
    )
    product = ForeignKey(
        to=Product,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='product_id'
        )
    )
    tax = ForeignKey(
        to=Tax,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='tax_id'
        )
    )
    tax_percent = DecimalField(
        verbose_name=_('Tax Percent'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='tax_percent',
            is_null=True,
            is_blank=True
        )
    )
    qty = DecimalField(
        verbose_name=_('Qty'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='qty',
            is_null=True,
            is_blank=True
        )
    )
    unit_price = DecimalField(
        verbose_name=_('Price Unit'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='unit_price',
            is_null=True,
            is_blank=True
        )
    )
    unit_price_with_tax = DecimalField(
        verbose_name=_('Price Unit With Tax'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='unit_price_with_tax',
            is_null=True,
            is_blank=True
        )
    )
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
    subtotal_with_tax = DecimalField(
        verbose_name=_('Subtotal with Tax'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='subtotal_with_tax',
            is_null=True,
            is_blank=True
        )
    )
    user = ForeignKey(
        to=User,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name,
            field='user_id'
        )
    )
