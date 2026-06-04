import logging

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Expense
from .forms import ExpenseForm
from .services import ExpenseService


logger = logging.getLogger(__name__)


def home(request):

    expenses = Expense.objects.all()

    category = request.GET.get("category")

    if category:
        expenses = expenses.filter(
            category__icontains=category
        )

    total = ExpenseService.total_expense()

    return render(
        request,
        "expensesApp/home.html",
        {
            "expenses": expenses,
            "total": total
        }
    )


def add_expense(request):

    try:

        if request.method == "POST":

            form = ExpenseForm(request.POST)

            if form.is_valid():

                form.save()

                logger.info(
                    "Expense Added Successfully"
                )

                return redirect("home")

        else:

            form = ExpenseForm()

        return render(
            request,
            "expensesApp/add_expense.html",
            {"form": form}
        )

    except Exception as e:

        logger.error(str(e))

        return render(
            request,
            "expensesApp/add_expense.html",
            {"error": str(e)}
        )


def update_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk
    )

    form = ExpenseForm(
        request.POST or None,
        instance=expense
    )

    if form.is_valid():

        form.save()

        return redirect("home")

    return render(
        request,
        "expensesApp/update_expense.html",
        {"form": form}
    )


def delete_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk
    )

    expense.delete()

    return redirect("home")