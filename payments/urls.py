from django.urls import path
from .views import PaymentCreateView, PaymentHistoryView

urlpatterns = [
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<str:account_number>/', PaymentHistoryView.as_view(), name='payment-history'),
]
