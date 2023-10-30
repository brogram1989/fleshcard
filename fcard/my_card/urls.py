from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addnw/', views.add, name='add'),
    path('testing/', views.testing, name='testing'),
    path('<str:smth>/', views.wordpage, name='wordpage'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),

]

