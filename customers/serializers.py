from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'account_number', 'issue_date', 'interest_rate', 'tenure', 'emi_due']
