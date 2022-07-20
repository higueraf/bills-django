from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.models import Country
from common.pagination import CustomPagination
from common.serializers import CountrySerializer



class CountryRecordsViewSet(
    generics.ListAPIView,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })
        return self.list(request)

    def post(self, request):
        return Response({
            'data': self.create(request).data
        })

    def put(self, request, pk=None):
        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)