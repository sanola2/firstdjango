from django.urls import path
from . import views


urlpatterns = [
  path('list/', views.list, name='list'),
  path('create/', views.create, name='create'),
  path('confirm/', views.confirm, name='confirm'),
  path('post/<int:post_id>/', views.post, name='post'),
]
