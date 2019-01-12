from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('store', views.store, name='store'),
    path('list', views.list, name='list'),
]