from django.urls import include, path
from rest_framework import routers
from config.views import index
from bills.urls import *
from common.urls import *
from companies.urls import *
from users.urls import *


urlpatterns = [
    path('', index),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include([
        # Common
        path('countries', include(countries_patterns)),
        path('states', include(states_patterns)),
        path('municipalities', include(municipalities_patterns)),
        path('parishes', include(parishes_patterns)),
        path('taxes', include(taxes_patterns)),
        # Companies
        path('companies', include(companies_patterns)),
        path('clients', include(clients_patterns)),
        # Bills
        path('bills', include(bills_patterns)),
        path('types-payments', include(types_payments_patterns)),
        path('products', include(products_patterns)),
        
        # Users
        path('users', include(users_patterns)),

    ]
    )
    )

]
