from dataclasses import fields
import email
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Customer, Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ordered_by', 'shipping_address', 'mobile', 'email']

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        username = forms.CharField(widget=forms.TextInput())
        password = forms.CharField(widget=forms.TextInput())
        email = forms.CharField(widget=forms.EmailInput()) 
        
        model = Customer
        fields = ['username', 'password','email','full_name', 'address']