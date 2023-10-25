from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testing/', views.testing, name='testing'),
    path('addnw/', views.add, name='add'),
    path('upd/', views.update, name='update'),
    path('delt/', views.delate, name='delate'),
    path('<str:smth>/', views.wordpage, name='wordpage'),
]

