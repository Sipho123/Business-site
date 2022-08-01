from multiprocessing import context
from pipes import Template
from re import template
from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView




class StoreView(TemplateView):
    template_name ="store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        return  context

class AllProductsView(TemplateView):
    template_name ="allproducts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = Categories.objects.all()
        return  context