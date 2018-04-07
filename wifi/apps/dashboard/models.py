from django.contrib.auth.models import User
from django.db import models


class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    name = models.CharField(max_length=64, null=False)
    ad_link = models.CharField(max_length=256, null=False)

    def create_ad_statistic(self):
        Statistic.objects.create(advertisement_id=self.id)
        UserSettings.objects.create(user=self.user)


class Statistic(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete='CASCADE')
    views = models.IntegerField(default=0)


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    ads_remain = models.IntegerField(default=5)
    views_remain = models.IntegerField(default=1000)
