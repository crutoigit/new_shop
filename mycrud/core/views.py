from django.shortcuts import render,redirect
from item.models import Category, Item

from .forms import SingupForm

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request,'core/index.html',{'items':items, 'categories':categories})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')  # redirect se face la un view care deja deseneaza un html
    else:
        form = SingupForm()
        
    return render(request, 'core/signup.html', {'form':form})