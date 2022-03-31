from django.db import models


# Create your models here.


class AdRequest(models.Model):
    username = models.CharField(max_length=255)
    sdk_version = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    error = models.CharField(max_length=255, null=True, blank=True)
    duration = models.BigIntegerField()
    media_files = models.URLField(null=True, blank=True)


class Impression(models.Model):
    username = models.CharField(max_length=255)
    sdk_version = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
