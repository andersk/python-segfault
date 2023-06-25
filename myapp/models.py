from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models import CASCADE


class Group(models.Model):
    groupname = models.TextField()


class MyUser(AbstractBaseUser):
    USERNAME_FIELD = "username"
    username = models.TextField(unique=True)
    group = models.ForeignKey(Group, on_delete=CASCADE)
