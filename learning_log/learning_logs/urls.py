"""Определяет схемы url для learning_logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    path(r'new_topics/', views.new_topic, name='new_topic'),
    
]
