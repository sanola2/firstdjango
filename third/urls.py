from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
  path('list/', views.list, name='list'),
  path('create/', views.create, name='restaurant-create'),
  path('update/', views.update, name='restaurant-update'),
  path('delete/', views.delete, name='restaurant-delete'),
  path('restaurant/<int:id>/', views.detail, name='restaurant-detail'),
  path('restaurant/<int:restaurant_id>/review/create', views.review_create, name='restaurant-create'),
  path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name='review-delete'),
  
  path('review/list/', views.review_list, name='review-list'),
]
