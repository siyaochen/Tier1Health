from django.conf import settings
from django.db import models
from django.utils import timezone


class Statistic(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    weight = models.IntegerField()
    bmi = models.IntegerField()
    nutrition = models.IntegerField()
    exercise = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

class Revenue(models.Model):
    MonthlyRevenue = models.CharField(max_length=50)
    Month = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.MonthlyRevenue, self.Month)
