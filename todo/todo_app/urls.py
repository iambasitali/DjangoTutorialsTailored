from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-item/', views.add_item, name='add_item'),
]
