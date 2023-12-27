from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Expenses
from .serializer import ExpenseSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

class Show_All_Expense_View(APIView):
    def get(self,request):
        list_of_entries = Expenses.objects.all()
        serializer = ExpenseSerializer(list_of_entries,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class Get_Single_entry(APIView):
    def post(self,request):
        serializer = ExpenseSerializer(data=request.post)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class Filter_By_Months(APIView):
    def get(self,request,month,year):
        starting_month = '01/'+ month + '/' + year
        ending_month = '30/'+ month + '/' + year
        datetime.strptime(starting_month,'%d/%m/%Y')
        serch_result = Expenses.objects.filter(created_at__time__range=(starting_month,ending_month))
        serializer = ExpenseSerializer(serch_result,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)