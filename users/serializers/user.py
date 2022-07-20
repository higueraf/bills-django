from common.serializers import DynamicFieldsSerializer
from users.models import User


class UserSerializer(DynamicFieldsSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
