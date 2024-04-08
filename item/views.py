from django.shortcuts import render,get_object_or_404
from .models import Item

# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    items_category = Item.objects.filter(category=item.category)
    items_category = items_category.exclude(name=item.name)
    return render(request, 'item/detail.html', {'item': item, 'items_category': items_category})
