from django.shortcuts import get_object_or_404
from .serializers import QuestionsSerializer, AnswersSerializer, UserSignupSerializer
from .models import Questions, Answers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def signup_view(request):
    if request.method == 'POST':
        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response()


@api_view(['GET', 'POST'])
def get_all_questions_view(request):
    if request.method == 'GET':
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
    
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def get_selected_question_view(request, questionID):
    quiz = get_object_or_404(Questions, id=questionID)

    if request.method == 'GET':
        serializer = QuestionsSerializer(quiz)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def post_answers_view(request, questionID):
    quiz = get_object_or_404(Questions, id=questionID)

    if request.method == 'GET':
        post_answer = Answers.objects.get(author_id=quiz)
        serializer = AnswersSerializer(post_answer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'POST':
        answer_obj = Answers.objects.get(author_id=quiz)
        serializer = AnswersSerializer(answer_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def update_answers_view(request, questionID, answerID):
    answ = Answers.objects.get(author_id=questionID)

    if request.method == 'PUT':
        serializer = AnswersSerializer(answ, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        answ.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

