from django.contrib.auth.models import User
from django.db import models


class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    name = models.CharField(max_length=64, null=False)
    ad_link = models.CharField(max_length=256, null=False)

    def create_ad_statistic(self):
        Statistic.objects.create(advertisement_id=self.id)


class Statistic(models.Model):
    advertisement = models.OneToOneField(Advertisement, on_delete='CASCADE', related_name='ad_statisic')
    views = models.IntegerField(default=0)


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE', related_name='settings')
    ads_remain = models.IntegerField(default=5)
    views_remain = models.IntegerField(default=1000)
