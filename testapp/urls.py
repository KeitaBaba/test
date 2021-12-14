from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.new, name='new'),
    path('create', views.create, name='create'),
]