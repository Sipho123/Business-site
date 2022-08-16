from django.urls import path
from xml.etree.ElementInclude import include
from django.views import View

from .views import(        
StoreView,
AllProductsView,
ProductDetailView,
AddToCartView,
MyCartView,
ManageCartView,

)

app_name = 'our_store'
urlpatterns = [
        path('store/', StoreView.as_view(), name='store'),
        path('all-products/', AllProductsView.as_view(), name='allproducts'),
        path('product/<slug:slug>/', ProductDetailView.as_view(), name='productdetail'),
        path('add-to-cart-<int:pro_id>/', AddToCartView.as_view(), name='addtocart'),
        path('my-cart/', MyCartView.as_view(), name='mycart'),
        path('manage-cart/<int:cp_id>/', ManageCartView.as_view(), name='managecart'),


]


