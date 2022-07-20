from rest_framework.serializers import PrimaryKeyRelatedField
from common.serializers import DynamicFieldsSerializer, StateSerializer
from common.models import Municipality, State


class MunicipalitySerializer(DynamicFieldsSerializer):

    state_id = PrimaryKeyRelatedField(queryset=State.objects.all(), write_only=True, source='state')
    state = StateSerializer(read_only=True, many=False,  fields=('id', 'name'))  


    class Meta:
        model = Municipality
        exclude = ('created_at', 'updated_at')
