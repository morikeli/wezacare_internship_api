from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Questions(models.Model):
    id = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    question = models.TextField(blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Questions'
        ordering = ['author']
    
    def __str__(self):
        return f'{self.author}'


class Answers(models.Model):
    id = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    author = models.ForeignKey(Questions, on_delete=models.CASCADE, editable=False)
    answer = models.TextField(blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Answers'
        ordering = ['author']

    def __str__(self):
        return f'{self.author}'