from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User
import jwt
from datetime import datetime, timedelta

class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.login_url = reverse('user_login')
        self.questions_url = '/questions/'+"5BAD9524B2"

        self.user_data = {
            "email": "testuser@gmail.com",
            "username": "testuser",
            "password": "morikeli",
            # "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjNDQzExNEQ4NkEiLCJleHAiOjE2Nzg4MDM5MzksImlhdCI6MTY3ODgwMDMzOX0.\
            # gfrtNLFOkYEslJbOX99IWXTCZT4OMpvgWvnok2I6lkI"
            
        }

        self.questions_data = {
            "id": "5BAD9524B2",
            "author": "3CC114D86A",
            "question": "Question 2",
        }
    
        return super().setUp()

    def test_signup(self):
        res = self.client.post(self.register_url, self.user_data)
        import pdb
        pdb.set_trace()
        self.assertEqual(res.status_code, 201)
    