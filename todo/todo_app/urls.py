from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('add-category/', views.addCategory, name='addCategory'),
    path('post-category/', views.postAddCategory, name='postAddCategory'),
    path('add-item/', views.addItem, name='addItem'),
    path('add-alert/', views.addAlert, name='addAlert'),
]
