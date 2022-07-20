from django.urls import path
from common.views import country, state, municipality, parish, tax


countries_patterns = [
    path('', country.CountryRecordsViewSet.as_view()),
    path('/<int:pk>', country.CountryRecordsViewSet.as_view()),
]

states_patterns = [
    path('', state.StateRecordsViewSet.as_view()),
    path('/<int:pk>', state.StateRecordsViewSet.as_view()),
]

municipalities_patterns = [
    path('', municipality.MunicipalityRecordsViewSet.as_view()),
    path('/<int:pk>', municipality.MunicipalityRecordsViewSet.as_view()),
]

parishes_patterns = [
    path('', parish.ParishRecordsViewSet.as_view()),
    path('/<int:pk>', parish.ParishRecordsViewSet.as_view()),
]

taxes_patterns = [
    path('', tax.TaxRecordsViewSet.as_view()),
    path('/<int:pk>', tax.TaxRecordsViewSet.as_view())
]

