# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
#from .models import UserDetails,ExpenseType

def index(request):
    return render(request,'index.html')
def CreateAccount(request):
    return render(request,'Details.html')
def savedetails(request):
    Account_id1=request.POST["t1"]
    username1=request.POST["t2"]
    d=UserDetails(Account_id1= Account_id ,username= username1)
    d.save()
    return HttpResponse(request,"succussfully save in database")

def Home_Page(request):
    return render(request,"Home_Page.html")
def EnterExpensesDetails(request):
    return render(request,"EnterExpenses.html")

def Storedetails(request):
    User_ID1=request.POST["u1"]
    Dinner1=request.POST["t3"]
    Trip1=request.POST["t4"]
    Shopping1=request.POST["t5"]
    data=ExpenseType(User_ID=User_ID1,Dinner= Dinner1,Trip=Trip1,Shopping=Shopping1)
    data.save()
    return HttpResponse(request,"Home_Page.html")

def Calculation(request):
    return render(request,"CalculateExp.html")

def calculate_expense(request):
    global sum
    uid=request.POST["u1"]
    result=ExpenseType.objects.get(User_ID=uid)
    Dinner=result.Dinner
    Trip=result.Trip
    Shopping=result.Shopping
    sum=Dinner+Trip+Shopping
    t={'Dinner':Dinner,'Trip':Trip,'Shopping':Shopping,'total':sum}
    return render(request,Total.html",{'t':t})

def split_expense(request):
    members=request.GET["t6"]
    Each_Share=int(sum)/int(members)
    return render(request,"Individual.html",{'Individual_share_Amount':Individual_share_Amount})






