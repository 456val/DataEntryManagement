from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import currency_notes, production_records, inventory

from django.shortcuts import render, redirect
from .forms import InventoryForm, ProductionForm, CurrencyForm  # type: ignore

def currency_view(request, currency_id):
    note = currency_notes.objects.get(id=currency_id)
    return render(request, 'currency.html', {'note': note})
    
def production_view(request, production_id):
    records = production_records.objects.get(id=production_id)
    return render(request, 'production.html', {'records': records})
    
def inventory_view(request, inventory_id):
    invent = inventory.objects.get(id=inventory_id)
    return render(request, 'inventory.html', {'invent': invent})
  
def home_view(request):
    return render(request, 'home.html')# Simple response for the root  


def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = InventoryForm()
    return render(request, 'add_inventory.html', {'form': form})


def add_currency(request):
    if request.method== 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        
    else:
        form= CurrencyForm()
    return render(request, 'add_currency.html', {'form': form})   

def add_production(request):
    if request.method== 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        
    else:
        form= ProductionForm()
    return render(request, 'add_production.html', {'form': form})   