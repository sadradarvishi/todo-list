from django.db import models

from todo_app.common_entity import CommonEntity
from todo_app.entity.user_entity import UserEntity

class TaskEntity(CommonEntity):
    owner = models.ForeignKey(UserEntity,on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    notes = models.TextField(blank=True)
    due_at = models.DateTimeField(null=True, blank=True)
    remind_at = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title