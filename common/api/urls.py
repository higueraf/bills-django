from django.urls import path
from rest_framework.routers import DefaultRouter
from common.api.country import CountryViewSet

router = DefaultRouter()
router.register(r'country', CountryViewSet,basename='countries')
urlpatterns = router.urls

"""
from common.api.country import (CountryListView, CountryDetailView, CountryCreateView,
                                CountryUpdateView, CountryDeleteView)

urlpatterns = [
    path('country/', CountryListView.as_view()),
    path('create/', CountryListView.as_view()),
    path('country/<pk>', CountryDetailView.as_view()),
    path('country/<pk>/update/', CountryUpdateView.as_view()),
    path('country/<pk>/delete/', CountryDeleteView.as_view()),
]

"""