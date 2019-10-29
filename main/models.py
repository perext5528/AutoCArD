from django.db import models


class UserInfo(models.Model):
    user_email = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_pw = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)
    user_history = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
