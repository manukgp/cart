from django import forms 
from .models import ShoppingItem 

class ShoppingForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['item', 'description', 'price', 'discount']
