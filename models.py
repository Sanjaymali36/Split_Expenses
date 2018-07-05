# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from expense_record_app import views
class UserDetails(models.Model):
    Account_id = models.IntegerField(primary_key=True)
    username =models.CharField(max_length=15)
   
class ExpenseType(models.Model):
    username = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    Dinner = models.IntegerField(max_length=5)
    Trip = models.IntegerField(max_length=5,default=0)
    Shopping = models.IntegerField(max_length=5,default=0)
    
    
