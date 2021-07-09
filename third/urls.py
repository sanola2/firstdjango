from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
  path('list/', views.list, name='list'),
  path('create/', views.create, name='restaurant-create'),
  path('update/', views.update, name='restaurant-update'),
  path('delete/', views.delete, name='restaurant-delete'),
]
