from django.conf import settings
from django.db import models
from django.utils import timezone

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=1000)
    description = models.TextField(default='Нет описания')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

