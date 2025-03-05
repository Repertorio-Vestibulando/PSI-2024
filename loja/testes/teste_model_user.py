from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTestClass(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='test')
    def test_user_exist(self):
        user = User.objects.first()
        self.assertTrue(user)
        print('Tudo certo no user👍')
