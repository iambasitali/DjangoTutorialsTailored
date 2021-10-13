from .models import Category, Item, Alert
from django import forms


class CategoryAddForm(forms.ModelForm):
    name = forms.CharField(label='Category Name', max_length=200)
    is_delete = forms.BooleanField(required=False)

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