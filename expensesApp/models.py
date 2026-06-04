from django.db import models
from django.core.validators import MinValueValidator


class Expense(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, db_index=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    description = models.TextField(blank=True)
    expense_date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-expense_date']


    def __str__(self):
        return f"{self.title} - {self.amount}"