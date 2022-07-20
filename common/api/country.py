from  rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from common.models import Country
from common.serializers import CountrySerializer
"""
class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryCreateView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdateView(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDeleteView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
"""

from rest_framework import viewsets

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer