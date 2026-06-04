import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from expensesApp.models import Expense
from .serializers import ExpenseSerializer

from django.db.models import Sum


# Set up logging
logger = logging.getLogger(__name__)


# Get all expenses or create a new expense
class ExpenseListCreateAPI(APIView):

    def get(self, request):
        try:
            logger.info("Fetching all expenses")
            expenses = Expense.objects.all()
            serializer = ExpenseSerializer(expenses, many=True)      # Serialize the queryset, many=True indicates that we are serializing a list of objects

            return Response(serializer.data)
        
        except Expense.DoesNotExist:
            return Response({"error": "Expense not found"},status=404)


    def post(self, request):
        try:
            logger.info("Creating a new expense")
            serializer = ExpenseSerializer(data=request.data)      # Deserialize the incoming data

            if serializer.is_valid():
                expense = serializer.save()
                logger.info(f"Expense created successfully | ID={expense.id}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)      # Return the created object with a 201 status code

            logger.warning(f"Validation Failed | {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Error creating expense | {str(e)}")
            return Response({"error": {str(e)}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Get, update, or delete a specific expense by ID
class ExpenseDetailAPI(APIView):

    def get_object(self, pk):

        return Expense.objects.get(pk=pk)


    def get(self, request, pk):

        logger.info(f"Fetching expense | ID={pk}")
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)

        return Response(serializer.data)


    def put(self, request, pk):
        logger.info(f"Expense Updated | ID={pk}")
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense, data=request.data)     # Deserialize the incoming data and update the existing object

        serializer.is_valid(raise_exception=True)
        # If the data is valid, save the updated object to the database
        serializer.save()

        return Response(serializer.data)


    def delete(self, request, pk):
        try:
            logger.info(f"Expense Deleted | ID={pk}")
            expense = self.get_object(pk)
            expense.delete()
            

            return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
        
        except Expense.DoesNotExist:
            logger.error(f"Expense Not Found | ID={pk}")
            return Response({"error": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)


# Search expenses by category

class ExpenseSearchAPI(APIView):

    def get(self, request):

        category = request.GET.get("category")
        if not category:
            return Response({"error": "Category parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        expenses = Expense.objects.filter(category__icontains=category)

        serializer = ExpenseSerializer(expenses,many=True)

        return Response(serializer.data)
    


# Get total expenses and summary


class ExpenseSummaryAPI(APIView):

    def get(self, request):

        total = Expense.objects.aggregate(total=Sum('amount'))

        return Response(total)
    


# Get total expenses by category

class CategorySummaryAPI(APIView):

    def get(self, request):

        data = Expense.objects.values('category').annotate(total=Sum('amount'))

        return Response(data)