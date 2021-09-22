from django import template
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import CategoryAddForm, ItemAddForm
from django.utils import timezone
from django.core import serializers

import json
from .models import Category


def index(request):

    list_of_category_objects = Category.objects.all()
    context = {
        'categories': list_of_category_objects
    }
    return render(request,'index.html', context)

def temp(request):
    list_of_category_objects = Category.objects.all()
    
    output = serializers.serialize('json', list_of_category_objects, fields=('name'))
    output = json.dumps(json.loads(output), indent=4)
    return HttpResponse(output, content_type="application/json")

    list_of_category_objects = Category.objects.filter()
    return render(request, 'index.html', {'categories': list_of_category_objects})


def detail(request, id):
    category = get_object_or_404(Category,id=id)
    return render(request, 'details.html', {'category': category})


def add_category(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.pub_date = timezone.now()
            category.save()
            return redirect('index')
    else:
        form = CategoryAddForm()
        return render(request, 'add_category.html', {'form': form})


def add_item(request):
    if request.method == 'POST':
        form = ItemAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemAddForm()
        return render(request, 'add_item.html', {'form': form})
