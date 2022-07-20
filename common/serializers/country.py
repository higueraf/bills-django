from common.serializers import DynamicFieldsSerializer
from common.models import Country

class CountrySerializer(DynamicFieldsSerializer):
    class Meta:
        model = Country
        exclude = ('created_at', 'updated_at')