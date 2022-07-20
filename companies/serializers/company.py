from rest_framework.serializers import PrimaryKeyRelatedField
from common.models import Country, State, Municipality, Parish
from common.serializers import DynamicFieldsSerializer, \
                                CountrySerializer, \
                                StateSerializer, \
                                MunicipalitySerializer, \
                                ParishSerializer

from companies.models.company import Company


class CompanySerializer(DynamicFieldsSerializer):
    
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


    class Meta:
        model = Company
        exclude = ('created_at', 'updated_at')
