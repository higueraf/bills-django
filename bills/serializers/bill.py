from rest_framework.serializers import PrimaryKeyRelatedField
from common.serializers import DynamicFieldsSerializer
from bills.models import Bill, TypePayment
from bills.serializers import BillDetailSerializer, TypePaymentSerializer
from companies.models import Company, Client
from companies.serializers import CompanySerializer, ClientSerializer
from users.models.user import User
from users.serializers.user import UserSerializer

class BillSerializer(DynamicFieldsSerializer):
    
    bill_details = BillDetailSerializer(many=True, read_only=True)
    client_id = PrimaryKeyRelatedField(queryset=Client.objects.all(),
        write_only=True, source='client')
    client = ClientSerializer(read_only=True, many=False,
        fields=('id', 'name'))
    type_payment_id = PrimaryKeyRelatedField(queryset=TypePayment.objects.all(),
        write_only=True, source='type_payment')
    type_payment = TypePaymentSerializer(read_only=True, many=False,
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
        model = Bill
        exclude = ('created_at', 'updated_at')

    