from rest_framework.serializers import PrimaryKeyRelatedField
from common.models import Tax
from common.serializers import DynamicFieldsSerializer, TaxSerializer
from bills.models import Bill, BillDetail, Product
from bills.serializers import ProductSerializer
from users.models.user import User
from users.serializers.user import UserSerializer

class BillDetailSerializer(DynamicFieldsSerializer):

    bill_id = PrimaryKeyRelatedField(queryset=Bill.objects.all(),
        write_only=True, source='bill')
    bill = ProductSerializer(read_only=True, many=False,
        fields=('id'))
    product_id = PrimaryKeyRelatedField(queryset=Product.objects.all(),
        write_only=True, source='product')
    product = ProductSerializer(read_only=True, many=False,
        fields=('id', 'name', 'price'))
    tax_id = PrimaryKeyRelatedField(queryset=Tax.objects.all(),
        write_only=True, source='tax')
    tax = TaxSerializer(read_only=True, many=False,
        fields=('id', 'name', 'percent'))
    user_id = PrimaryKeyRelatedField(queryset=User.objects.all(),
        write_only=True, source='user')
    user = UserSerializer(read_only=True, many=False,
        fields=('id', 'first_name','last_name', 'email'))

    class Meta:
        model = BillDetail
        exclude = ('updated_at',)

