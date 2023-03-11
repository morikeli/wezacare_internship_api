from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.login_url = reverse('user_login')

        self.user_data = {
            "email": "sarahj@gmail.com",
            "username": "sarahj",
            "password": "morikeli",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestView(TestSetup):
    def test_user_signup(self):
        res = self.client.post(self.register_url, self.user_data)
        self.assertEqual(res.status_code, 201)

    def test_user_can_login(self):
        res = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(res.status_code, 401)
