from django.db import models


class Customer(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tenure = models.IntegerField(help_text="Loan tenure in months")
    emi_due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Customer - {self.account_number}"
