from common.serializers import DynamicFieldsSerializer
from common.models import Tax

class TaxSerializer(DynamicFieldsSerializer):
    class Meta:
        model = Tax
        exclude = ('created_at', 'updated_at')