from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(source='customer.account_number', read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'account_number', 'payment_date', 'payment_amount', 'status']


class PaymentCreateSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(write_only=True)

    class Meta:
        model = Payment
        fields = ['account_number', 'payment_amount', 'status']

    def validate_account_number(self, value):
        from customers.models import Customer
        if not Customer.objects.filter(account_number=value).exists():
            raise serializers.ValidationError("Customer with this account number does not exist.")
        return value

    def create(self, validated_data):
        from customers.models import Customer
        account_number = validated_data.pop('account_number')
        customer = Customer.objects.get(account_number=account_number)
        payment = Payment.objects.create(customer=customer, **validated_data)
        return payment
