from django.urls import path
from companies.views import company, client

companies_patterns = [
    path('', company.CompanyRecordsViewSet.as_view()),
    path('/<int:pk>', company.CompanyRecordsViewSet.as_view())
]

clients_patterns = [
    path('', client.ClientRecordsViewSet.as_view()),
    path('/<int:pk>', client.ClientRecordsViewSet.as_view())
]
