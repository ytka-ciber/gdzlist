from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100, default='Имя ссылки')
    stars = models.IntegerField(default=5)
    review = models.CharField(max_length=1000, default='Отзыв')

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=1000)
    description = models.TextField(default='Нет описания')
    stars = models.IntegerField(default=5)
