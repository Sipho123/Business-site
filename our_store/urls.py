from django.urls import path
from xml.etree.ElementInclude import include
from  . import views

urlpatterns = [
        path('store/', views.store, name='store-view'),
        path('cart/', views.cart, name='cart-view'),
        path('update_item/', views.updateItem, name="update_item"),
        path('checkout/', views.checkout, name="checkout-view"),
]


