from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    username = models.CharField(max_length=150, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Questions(models.Model):
    """
        A given user can ask many questions. ForeignKey class is used to establish one-to-many relationship.
        In this case, one user can ask many questions (one-to-many relationship).
        Fields:
            - author: user who posted the question.
            - question: the question asked.
            - posted: date and time when the question was posted.
            - edited: date and time the author of the question updated the question
    """
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
    """
        A given user can post many answers. ForeignKey class is used to establish one-to-many relationship.
        In this case, one user can ask many answers (one-to-many relationship).
        Fields:
            - author: the question asked.
            - answered_by: user who posted the answer to a given question.
            - answer: the answer asked.
            - posted: date and time when the answer was posted.
            - edited: date and time the author updated the his/her response.
    """
    id = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    author = models.ForeignKey(Questions, on_delete=models.CASCADE, editable=False)
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    answer = models.TextField(blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Answers'
        ordering = ['author']

    def __str__(self):
        return f'{self.author}'