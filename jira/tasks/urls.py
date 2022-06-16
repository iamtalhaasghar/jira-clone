from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.list_todos, name='todos')
]
