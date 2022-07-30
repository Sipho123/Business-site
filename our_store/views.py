from multiprocessing import context
from django.shortcuts import render
from .models import Item

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'item_list.html', context)

def store(request):
    
    context = {'items': Item.objects.all()}
    return render(request, 'our_store/store.html', context)