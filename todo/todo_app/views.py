from django import template
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import CategoryAddForm, ItemAddForm, AlertAddForm
from django.utils import timezone
from django.core import serializers

import json
from .models import Category


def index(request):

    list_of_category_objects = Category.objects.all()
    context = {
        'categories': list_of_category_objects
    }
    return render(request,'todo_app/index.html', context)

def temp(request):
    list_of_category_objects = Category.objects.all()
    
    output = serializers.serialize('json', list_of_category_objects, fields=('name'))
    output = json.dumps(json.loads(output), indent=4)
    return HttpResponse(output, content_type="application/json")

    list_of_category_objects = Category.objects.filter()
    return render(request, 'todo_app/index.html', {'categories': list_of_category_objects})


def detail(request, id):
    category = get_object_or_404(Category,id=id)
    return render(request, 'todo_app/details.html', {'category': category})


def addCategory(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.pub_date = timezone.now()
            category.save()
        return redirect('index')
    else:
        form = CategoryAddForm()
        return render(request, 'todo_app/add_category.html', {'form': form})

def postAddCategory(request):
    form = CategoryAddForm(request.POST)
    category = form.save(commit=False)
    category.pub_date = timezone.now()
    category.save()
    return redirect('index')

def addItem(request):
    if request.method == 'POST':
        form = ItemAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemAddForm()
        return render(request, 'todo_app/add_item.html', {'form': form})


def addAlert(request):
    if request.method == 'POST':
        form = AlertAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlertAddForm()
        return render(request, 'todo_app/add_alert.html', {'form': form})
