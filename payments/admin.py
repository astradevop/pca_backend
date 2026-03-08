from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['customer', 'payment_date', 'payment_amount', 'status']
    list_filter = ['status', 'payment_date']
    search_fields = ['customer__account_number']
