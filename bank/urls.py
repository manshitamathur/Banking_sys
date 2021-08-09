from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views



urlpatterns = [
    
    #path('home/', views.home),
    url('view_all_customers/$', views.view_all_customers),
    path('view_customer/<user2>/', views.view_customer),
    path('make_transaction_filled/<user2>/', views.make_transaction_filled),
     url('transfer/$', views.transfer),
     url('view_your_account_details/$', views.view_your_account_details),
     url('view_your_account_details_page/$', views.view_your_account_details_page),
     url('view_transactions_page/$', views.view_transactions_page),
     url('view_transactions/$', views.view_transactions),
    # #url('contact/$', views.contact),
    #url('about/$', views.about),
]
