from django import views
from django.urls import path
from  . import views

urlpatterns = [
        path('item_list/', views.item_list, name='item-list'),
         path('store/', views.store, name='store-view'),
        ]

