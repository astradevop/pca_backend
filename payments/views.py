from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer, PaymentCreateSerializer


class PaymentCreateView(APIView):
    """
    POST /api/payments/
    Create a new payment for a customer by account number.

    Request Body:
        {
            "account_number": "ACC001",
            "payment_amount": 5000.00,
            "status": "completed"   (optional, defaults to "completed")
        }
    """

    def post(self, request):
        serializer = PaymentCreateSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
            response_serializer = PaymentSerializer(payment)
            return Response(
                {
                    "message": "Payment recorded successfully.",
                    "payment": response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentHistoryView(APIView):
    """
    GET /api/payments/<account_number>/
    Retrieve all payments for a specific customer account.
    """

    def get(self, request, account_number):
        payments = Payment.objects.filter(customer__account_number=account_number)
        if not payments.exists():
            return Response(
                {"message": f"No payment history found for account {account_number}."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
