from django.db.models import CharField, ForeignKey, TextField, PROTECT
from django.utils.translation import gettext_lazy as _
from common.models.models import CommonData, ErrorMessages
from common.models.country import Country
from common.models.state import State
from common.models.municipality import Municipality
from common.models.parish import Parish
from companies.models.company import Company
from users.models import User



class Client(CommonData):
    model_name = 'Client'
    first_name = CharField(
        verbose_name=_('First Name'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='first_name')
    )
    last_name = CharField(
        verbose_name=_('Last Name'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='last_name')
    )
    identification = CharField(
        verbose_name=_('Identification'),
        max_length=100,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='identification')
    )
    address = TextField(
        verbose_name=_('Address'),
        max_length=500,
        error_messages=ErrorMessages.get_char_field(model=model_name, field='address'))
    country = ForeignKey(
        to=Country,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='country_id')
    )
    state = ForeignKey(
        to=State,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='state_id')
    )
    municipality = ForeignKey(
        to=Municipality,
        on_delete=PROTECT,
        null=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='municipality_id')
    )
    parish = ForeignKey(
        to=Parish,
        on_delete=PROTECT,
        null=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='parish_id')
    )
    company = ForeignKey(
        to=Company,
        on_delete=PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='company_id')
    )
    user = ForeignKey(
        to=User,
        on_delete=PROTECT,
        null=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='user_id')
    )