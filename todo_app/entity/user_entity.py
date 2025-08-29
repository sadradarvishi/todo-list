from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from todo_app.common_entity import CommonEntity

class UserEntity(CommonEntity, AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=225, null=False)
    lastname = models.CharField(max_length=225, null=False)
    username = models.CharField(max_length=225, null=False, unique=True)
    password = models.CharField(max_length=225, null=False)
    email = models.EmailField(max_length=225, null=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
