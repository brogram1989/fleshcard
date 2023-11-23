from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/set_list/', views.set_list, name='set_list'),
    path('set_create/', views.set_create, name='set_create'),
    path('<int:id>/set_delete/', views.set_delete, name='set_delete'),
    path('<int:id>/set_update/', views.set_update, name='set_update'),
    path('<int:id>/set_list/addnw/', views.add, name='word_add'),
    path('testing/', views.testing, name='testing'),
    path('<str:smth>/', views.wordpage, name='wordpage'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]

