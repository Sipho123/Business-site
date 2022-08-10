from multiprocessing import context
from pipes import Template
from random import Random
from re import template
from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Cart


class StoreView(TemplateView):
    template_name ="store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all().order_by("-id")
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

class AddToCartView(TemplateView):
    template_name = "addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #get product id from requested url
        product_id = self.kwargs['pro_id']
        # get product
        product_obj = Product.objects.get(id=product_id)
        # check if cart exists
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            Cart_obj = Cart.objects.get(id=cart_id)
        else:
            Cart_obj = Cart.objects.create(total=0)
            self.request.session.get['cart_id'] = Cart_obj.id
        return context

        
        

