from django.shortcuts import get_object_or_404
from django.contrib import auth
from .serializers import QuestionsSerializer, AnswersSerializer, UserSignupSerializer
from .models import Questions, Answers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime, timedelta
import jwt


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is None:
            raise AuthenticationFailed('INVALID CREDENTIALS!!!')

        payload = {
            "id": user.id,
            "exp": datetime.utcnow() + timedelta(minutes=60),    # token expires after 1 hour.
            "iat": datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.data = {"User logged in ..."}

        # store token as a cookies
        response.set_cookie(key='jwt', value=token, httponly=True)

        return response


class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuestionsView(APIView):
    def get(self, request):
        quiz = Questions.objects.all()
        serializer = QuestionsSerializer(quiz, many=True)

        return Response(serializer.data)

    # Use BaseAuthentication System (i.e. username and password) to authenticate user and check whether s/he is authenticated (IsAuthenticated)
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = QuestionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return Response({"AnonymousUser. Please login to post question."})

class get_or_delete_QuestionsView(APIView):
    def get_quiz(self, questionID):
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
    def delete(self, request, questionID):        
        quiz = self.get_quiz(questionID)

        if request.user == quiz.author:
            quiz.delete()
            return Response({"You deleted this question!"}, status=status.HTTP_204_NO_CONTENT)

        else:
           return Response({"message": "You cannot delete this question"}, status=status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_204_NO_CONTENT)

class SendAnswersView(APIView):
    def get_quiz(self, questionID):
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
        try:
            return Answers.objects.get(id=answerID)
        
        except Answers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
            return Response({"ERROR: You cannot delete this message!"}, status=status.HTTP_403_FORBIDDEN)
    
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
    

