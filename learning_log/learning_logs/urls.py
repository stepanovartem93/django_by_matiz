"""Определяет схемы url для learning_logs"""
from django.urls import path,re_path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path(r'new_topic/', views.new_topic, name='new_topic'),
    # Страница добавления новой записи
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]
