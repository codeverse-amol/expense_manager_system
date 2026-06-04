from django.urls import path

from .api_views import *

urlpatterns = [

    path('expenses/', ExpenseListCreateAPI.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailAPI.as_view()),
    path('search/', ExpenseSearchAPI.as_view()),
    path('summary/', ExpenseSummaryAPI.as_view()),
    path('category-summary/', CategorySummaryAPI.as_view()),
]