from .models import Category, Item
from django import forms


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
