from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginTestClass(TestCase):
    def setUp(self):
        User.objects.create_user(username='rodrigo', password='calabreso')
        self.client = Client()
        
    def test_login(self):
        response = self.client.post('/login', {'username': 'rodrigo', 'password': 'calabreso'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        print('Tudo certo no login👍')