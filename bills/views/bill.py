from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.pagination import CustomPagination
from bills.models import Bill, bill
from bills.serializers import BillSerializer, BillDetailSerializer


class BillRecordsViewSet(
    generics.ListAPIView,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
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
        request.data['company_id'] = request.user.company.id
        request.data['user_id'] = request.user.id
        data = self.create(request).data
        for bill_detail in request.data['bill_details']:
            bill_detail['bill_id'] = data['id']
            bill_detail['user_id'] = request.user.id
            serializer = BillDetailSerializer(data=bill_detail)
            if serializer.is_valid():
                serializer.save()
        data = Bill.objects.get(pk=data['id'])
        return Response({
            'data': BillSerializer(data).data
        })

    def put(self, request, pk=None):
        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)