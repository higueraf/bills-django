from rest_framework.serializers import PrimaryKeyRelatedField
from common.serializers import DynamicFieldsSerializer, MunicipalitySerializer
from common.models import Parish, Municipality


class ParishSerializer(DynamicFieldsSerializer):

    municipality_id = PrimaryKeyRelatedField(queryset=Municipality.objects.all(), write_only=True, source='municipality')
    municipality = MunicipalitySerializer(read_only=True, many=False,  fields=('id', 'name'))  


    class Meta:
        model = Parish
        exclude = ('created_at', 'updated_at')
