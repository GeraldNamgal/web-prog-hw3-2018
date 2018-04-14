from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'priceSmall', 'priceLarge')
        widgets = {
	       'priceSmall': forms.RadioSelect(),
           'priceLarge': forms.RadioSelect()
        }

    # TODO: Process user input?
    #def processInput(self):
