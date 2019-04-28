# -*- coding: utf-8 -*-
from django.db import models

status_choice = (
    ('todo', 'add a new task'),
    ('finished', 'finished a task')
)

class Todo(models.Model):
    task_name = models.CharField(max_length=200, unique=True)
    contents = models.TextField()
    priority = models.IntegerField(default=1)
    create_time = models.DateField(auto_now_add=True)
    status = models.CharField(choices=status_choice, default='todo', max_length=100)
    end_time = models.DateField()

    def __unicode__(self):
        return self.task_name
    
