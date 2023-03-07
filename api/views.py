from django.shortcuts import get_object_or_404
from .serializers import QuestionsSerializer, AnswersSerializers
from .models import Questions, Answers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def get_all_questions_view(request):
    if request.method == 'GET':
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)

    elif request.method == 'POST':
        serializer = QuestionsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def get_selected_question_view(request, questionID):
    quiz = get_object_or_404(Questions, id=questionID)

    if request.method == 'GET':
        serializer = QuestionsSerializer(quiz)

    elif request.method == 'DELETE':
        quiz.delete()


    return Response(serializer.data)

