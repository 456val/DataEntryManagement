from django import forms
from .models import currency_notes, production_records, inventory

class CurrencyForm(forms.ModelForm):
    class Meta:
        model=currency_notes
        fields=['id', 'denomination', 'material', 'year_issued', 'quantity_produced']
        
class ProductionForm(forms.ModelForm):
    class Meta:
        model = production_records
        fields= ['id', 'currency_notes', 'date_produced', 'batch_number', 'quantity_produced']
        
class InventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields =['id', 'currency_notes', 'quantity_available', 'location']
        
        
    