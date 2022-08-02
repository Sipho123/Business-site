from django.urls import path
from xml.etree.ElementInclude import include
from django.views import View

from .views import(
        
StoreView,
AllProductsView,

)

app_name = 'our_store'
urlpatterns = [
        path('store/', StoreView.as_view(), name='store'),
        path('all-products/', AllProductsView.as_view(), name='allproducts'),
        path('products/<slug:slug>/', ProductDetailView.as_view(), name='productdetail'),

]
