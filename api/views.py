from django.shortcuts import get_object_or_404
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import QuestionsSerializer, AnswersSerializer, UserSignupSerializer, LoginSerializer
from .models import Questions, Answers
from datetime import datetime, timedelta
import jwt


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class QuestionsView(APIView):
    def get(self, request):     # a given user can get all the questions asked.
        quiz = Questions.objects.all()
        serializer = QuestionsSerializer(quiz, many=True)

        return Response(serializer.data)

    # Use BaseAuthentication System (i.e. username and password) to authenticate user and check whether s/he is authenticated (IsAuthenticated)
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):    # an authenticated user can post a question
        serializer = QuestionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class get_or_delete_QuestionsView(APIView):
    def get_quiz(self, questionID):
        # search for a question using an ID assigned to that question.
        try:
            return Questions.objects.get(id=questionID)
        except Questions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, questionID):
        # quiz = self.get_quiz(questionID)
        serializer = QuestionsSerializer(self.get_quiz(questionID))
        return Response(serializer.data)

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, questionID):        # only authenticated authors can delete a question they posted.
        quiz = self.get_quiz(questionID)

        if request.user == quiz.author:
            quiz.delete()
            return Response({"You deleted this question!"}, status=status.HTTP_204_NO_CONTENT)

        else:
           return Response({"message": "You cannot delete this question"}, status=status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_204_NO_CONTENT)

class SendAnswersView(APIView):
    def get_quiz(self, questionID):
        # search for a question using an ID assigned to that question.
        # if the question exists, an authenticated user can post their response to that question.
        try:
            return Questions.objects.get(id=questionID)
        except Questions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, questionID):
        serializer = QuestionsSerializer(self.get_quiz(questionID))
        return Response(serializer.data)

    # Checks if the user is authenticated. BasicAuthentication is the default authentication system.
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, questionID):
        serializer = AnswersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author_id=questionID, answered_by=request.user)    # author is the current logged in user.
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UpdateAndDeleteAnswersView(APIView):
    def get_answer(self, questionID, answerID):
        # search for an answer using an ID assigned to that answer.
        try:
            return Answers.objects.get(id=answerID)
        
        except Answers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # only authenticated authors can update answers they posted.
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, questionID, answerID):
        answ_obj = self.get_answer(questionID, answerID)

        if request.user == answ_obj.answered_by:
            answer_obj = Answers.objects.get(id=answerID, answered_by=request.user)
            serializer = AnswersSerializer(answer_obj, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        
        else:
            return Response({"ERROR: You cannot update this answer"}, status=status.HTTP_403_FORBIDDEN)
    
    # only authenticated authors can delete answers they posted.
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, questionID, answerID):
        answ = self.get_answer(questionID, answerID)

        if request.user == answ.answered_by:
            answ.delete()
            return Response({"You deleted this answer!"}, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({"You are not authorized to delete this answer"}, status=status.HTTP_403_FORBIDDEN)

class LogoutUserView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {"message": "User logged out ..."}

        return response
    