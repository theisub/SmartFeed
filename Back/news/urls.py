from django.urls import path

from . import views

urlpatterns = [
    path('init_user/', views.init_user, name='init_user'),
    path('get_news/', views.get_news, name='get_news'),
    path('news_click/', views.news_click, name='news_click'),
    path('get_user_tags/', views.get_user_tags, name='get_user_tags'),
]