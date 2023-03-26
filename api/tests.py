from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Questions
import jwt
from datetime import datetime, timedelta


class SignUpTestCase(APITestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.user_data = {
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": "morikeli"
        }
    
    def test_signup(self):
        res = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(res.status_code, 201)

class QuestionsTestCase(APITestCase):
    def setUp(self):
        self.get_all_questions_url = reverse('all_questions')
        # self.questions_id_url = reverse('get_question', "api.urls")
        self.user_data = {
            "username": "testuser",
            "password": "morikeli"
        }
        self.questions_data = {
            "id": "5BAD9524B2",
            "author": "3CC114D86A",
            "question": "TestCase question ..." 
        }

    def test_get_all_questions(self):
        res = self.client.get('/questions/'+ self.questions_data["id"])
        self.assertEqual(res.status_code, 200)

    # def test_author_can_delete_questions(self):
    #     res = self.client.delete(self.questions_url, self.user_data, format='json')
    #     # import pdb; pdb.set_trace()
    #     self.assertEqual(res.status_code, 403)

