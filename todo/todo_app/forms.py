from .models import Category, Item, Alert
from django import forms


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class AlertAddForm(forms.ModelForm):
    class Meta:
        model = Alert # This will bind the ModelForm base class with Alert Model.
        fields = '__all__' 