from rest_framework import serializers
from .models import Questions, Answers


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['question']


class AnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['answer']

