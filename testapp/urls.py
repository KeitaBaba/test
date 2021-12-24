from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.new, name='new'),
    path('create', views.create, name='create'),
    path('list', views.list, name='list'),
    path('delete/<int:pk>/', views.delete, name="delete"),
]