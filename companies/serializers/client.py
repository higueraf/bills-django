from rest_framework.serializers import PrimaryKeyRelatedField
from common.models import Country, State, Municipality, Parish
from common.serializers import DynamicFieldsSerializer, \
                                CountrySerializer, \
                                StateSerializer, \
                                MunicipalitySerializer, \
                                ParishSerializer

from companies.models.client import Client, Company
from companies.serializers import CompanySerializer
from users.models import User
from users.serializers import UserSerializer


class ClientSerializer(DynamicFieldsSerializer):
    
    country_id = PrimaryKeyRelatedField(queryset=Country.objects.all(),
        write_only=True, source='country', allow_null=True)
    country = CountrySerializer(read_only=True, many=False,
        fields=('id', 'name'))
    state_id = PrimaryKeyRelatedField(queryset=State.objects.all(),
        write_only=True, source='state', allow_null=True)
    state = StateSerializer(read_only=True, many=False,
        fields=('id', 'name'))
    municipality_id = PrimaryKeyRelatedField(
        queryset=Municipality.objects.all(),
        write_only=True, source='municipality', allow_null=True)
    municipality = MunicipalitySerializer(read_only=True, many=False,
        fields=('id', 'name'))
    parish_id = PrimaryKeyRelatedField(queryset=Parish.objects.all(),
        write_only=True, source='parish', allow_null=True)
    parish = ParishSerializer(read_only=True, many=False,
        fields=('id', 'name'))
    user_id = PrimaryKeyRelatedField(queryset=User.objects.all(),
        write_only=True, source='user')
    user = UserSerializer(read_only=True, many=False,
        fields=('id', 'first_name','last_name', 'email'))
    company_id = PrimaryKeyRelatedField(queryset=Company.objects.all(),
        write_only=True, source='company')
    company = CompanySerializer(read_only=True, many=False,
        fields=('id', 'name'))


    class Meta:
        model = Client
        exclude = ('created_at', 'updated_at')
