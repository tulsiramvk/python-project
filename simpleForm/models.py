from django.db import models

class userInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    mobile = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
 