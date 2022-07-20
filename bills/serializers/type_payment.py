from common.serializers import DynamicFieldsSerializer
from bills.models import TypePayment


class TypePaymentSerializer(DynamicFieldsSerializer):

    class Meta:
        model = TypePayment
        exclude = ('created_at', 'updated_at')

