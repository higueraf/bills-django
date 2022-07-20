from rest_framework import exceptions
from rest_framework.serializers import PrimaryKeyRelatedField
from common.serializers import DynamicFieldsSerializer, CountrySerializer
from common.models import State, Country


class StateSerializer(DynamicFieldsSerializer):

    country_id = PrimaryKeyRelatedField(queryset=Country.objects.all(), write_only=True, source='country')
    country = CountrySerializer(read_only=True, many=False,  fields=('id', 'name'))  


    class Meta:
        model = State
        exclude = ('created_at', 'updated_at')
