from django.db import models
from django.contrib.auth.models import User

"""Objects for database formation with makemigrations
    $python manage.py makemigrations
    $python manage.py sqlmigrate boards 0001
    $python manage.py migrate
"""
class Board(models.Model):
    name = models.CharField(max_length=100, unique = True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='topics')

    def __str__(self):
        return self.name

class Post(models.Model):
    message = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(null=True)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name='posts')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, on_delete = models.CASCADE, related_name='+')

    def __str__(self):
        return self.name


