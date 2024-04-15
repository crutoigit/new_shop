from django.shortcuts import render,redirect
from item.models import Category, Item
from django.contrib.auth import logout

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
            return redirect('/login/')  # redirect se face la un view care deja deseneaza un html
    else:
        form = SingupForm()
        
    return render(request, 'core/signup.html', {'form':form})

# logica de login este implementata dupa default in url-uri

def logout_user(request):
    logout(request)  #insusi delogarea
    return redirect('/') # dupa ce iesim din cont ajungem la pagina princiapla

    