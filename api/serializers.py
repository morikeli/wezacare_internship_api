from rest_framework import serializers
from .models import Questions, Answers


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'author', 'question', 'posted', 'edited']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'author', 'answer', 'posted', 'edited']

