from django.db.models import Sum

from .models import Expense


class ExpenseService:

    @staticmethod
    def total_expense():

        return Expense.objects.aggregate(
            total=Sum("amount")
        )["total"] or 0

    @staticmethod
    def category_summary():

        return Expense.objects.values(
            "category"
        ).annotate(
            total=Sum("amount")
        )