from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
  path('', views.main, name='main'),
  path('duruduru', views.duruduru, name='duruduru'),
  path('mochamilk', views.mochamilk, name='mochamilk'),
  path('duruduru/comment', views.comment_duruduru, name='comment_duruduru'),
  path('mochamilk/comment', views.comment_mochamilk, name='comment_mochamilk'),
]