from django.db import models
from customers.models import Customer


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    customer = models.ForeignKey(Customer, to_field='account_number', on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='completed')

    def __str__(self):
        return f"Payment by {self.customer.account_number} on {self.payment_date}"
