from django import forms

from .models import Items

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_image']