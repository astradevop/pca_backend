from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'issue_date', 'interest_rate', 'tenure', 'emi_due']
    search_fields = ['account_number']
