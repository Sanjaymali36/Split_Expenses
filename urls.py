"""monthly_expenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from expense_record_app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getpage/',views.index),
    url(r'^add/',views.CreateAccount),
    url(r'^insert/',views.savedetails),
    url(r'^ ',views.Home_Page),
    url(r'^EnterExpenses/',views.EnterExpensesDetails),
    url(r'^update/',views.Storedetails),
    url(r'update/CalculateExpenses/',views.Calculation)
    url(r'^total/',views.calculate_expense),
    url(r'^split/',views.split_expense)

]
