from rest_framework import serializers
from .models import Questions, Answers, User


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'author', 'question', 'posted', 'edited']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'author', 'answer', 'posted', 'edited']

