from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Solution(models.Model):
    SOLUTION_TYPES = [
        ('volunteer', 'Volunteer'),
        ('request', 'Request'),
        ('sell', 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solutions')
    solution_type = models.CharField(max_length=10, choices=SOLUTION_TYPES)
    description = models.TextField()
    terms = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount_to_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Amount for sell solution
    amount_willing_to_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Amount for request solution

    def __str__(self):
        return f"{self.solution_type.capitalize()} - {self.user.username}"

    def save(self, *args, **kwargs):
        # Ensure the correct amount field is set based on solution type
        if self.solution_type == 'sell' and self.amount_to_charge is None:
            raise ValueError("Amount to charge must be specified for sell solutions.")
        elif self.solution_type == 'request' and self.amount_willing_to_pay is None:
            raise ValueError("Amount willing to pay must be specified for request solutions.")
        super().save(*args, **kwargs)
