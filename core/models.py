from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class User(AbstractUser):
    # Mobile number validation with regex to ensure proper format
    mobile_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="Enter a valid mobile number in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    email = models.EmailField(unique=True)  # Enforce unique email addresses
    is_admin = models.BooleanField(default=False)  # For potential role-based access

    def __str__(self):
        return self.username


class Solution(models.Model):
    SOLUTION_TYPES = [
        ('volunteer', 'Volunteer'),
        ('request', 'Request'),
        ('sell', 'Sell'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='solutions'
    )
    solution_type = models.CharField(
        max_length=10,
        choices=SOLUTION_TYPES
    )
    description = models.TextField()
    terms = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount_to_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Required for 'sell' solutions"
    )
    amount_willing_to_pay = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Required for 'request' solutions"
    )

    def __str__(self):
        return f"{self.solution_type.capitalize()} - {self.user.username}"

    def clean(self):
        """
        Override clean method to perform validation logic before saving.
        """
        from django.core.exceptions import ValidationError

        if self.solution_type == 'sell' and self.amount_to_charge is None:
            raise ValidationError("Amount to charge must be specified for 'sell' solutions.")
        if self.solution_type == 'request' and self.amount_willing_to_pay is None:
            raise ValidationError("Amount willing to pay must be specified for 'request' solutions.")

    def save(self, *args, **kwargs):
        # Call clean method to enforce validation rules
        self.clean()
        super().save(*args, **kwargs)
