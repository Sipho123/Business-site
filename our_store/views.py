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
        context['allcategories'] = Category.objects.all()
        return  context


class ProductDetailView(TemplateView):
    template_name ="productdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        product.view_count += 1
        product.save()
        context['product'] = product
        return  context       