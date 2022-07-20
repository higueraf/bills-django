from django.urls import path
from bills.views import bill, type_payment, product

bills_patterns = [
    path('', bill.BillRecordsViewSet.as_view()),
    path('/<int:pk>', bill.BillRecordsViewSet.as_view())
]

types_payments_patterns = [
    path('', type_payment.TypePaymentRecordsViewSet.as_view()),
    path('/<int:pk>', type_payment.TypePaymentRecordsViewSet.as_view())
]

products_patterns = [
    path('', product.ProductRecordsViewSet.as_view()),
    path('/<int:pk>', product.ProductRecordsViewSet.as_view())
]
