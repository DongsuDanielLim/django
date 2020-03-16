from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('post/<int:pk>', views.post_detail, name='post_detail'),
  path('post/new', views.post_new, name='post_new'),
  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
  path('posting', views.posting_list, name='posting_list'),
  path('posting/<int:pk>', views.posting_detail, name='posting_detail'),
  path('map', views.map, name='map')
]