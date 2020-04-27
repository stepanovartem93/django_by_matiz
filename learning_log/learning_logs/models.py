from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text

class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """указывате как правильно выводить множественное число модели"""
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text[:50] + '...'