from numpy import source
from rest_framework.serializers import PrimaryKeyRelatedField
from common.serializers import DynamicFieldsSerializer
from common.models.tax import Tax
from bills.models import Product
from companies.models.company import Company
from companies.serializers.company import CompanySerializer
from common.serializers.tax import TaxSerializer
from users.models.user import User
from users.serializers.user import UserSerializer


class ProductSerializer(DynamicFieldsSerializer):
    
    tax_id = PrimaryKeyRelatedField(queryset=Tax.objects.all(),
         write_only=True, source='tax')
    tax = TaxSerializer(read_only=True, many=False,
        fields=('id', 'name', 'percent'))
    user_id = PrimaryKeyRelatedField(queryset=User.objects.all(),
        write_only=True, source='user')
    user = UserSerializer(read_only=True, many=False,
        fields=('id', 'first_name','last_name', 'email'))
    company_id = PrimaryKeyRelatedField(queryset=Company.objects.all(),
        write_only=True, source='company')
    company = CompanySerializer(read_only=True, many=False,
        fields=('id', 'name'))

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')
