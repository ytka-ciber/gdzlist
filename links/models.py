from django.conf import settings
from django.db import models
from django.utils import timezone


class Review(models.Model):
    name = models.CharField(max_length=100, default='Имя ссылки')
    review = models.CharField(max_length=1000, default='Отзыв')

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=1000)
    description = models.TextField(default='Нет описания')
    reviews = models.JSONField(default=[""])
