from django.conf import settings
from django.db import models
from django.utils import timezone

class Statistic(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    weight = models.CharField(max_length = 50)
    height = models.CharField(max_length = 50)

    def publish(self):
        self.save()