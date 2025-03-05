from django.test import TestCase, Client
from loja.models import Produto
from django.db import transaction, IntegrityError

class HomeViewTestClass(TestCase):
    def setUp(self):
        try:
            with transaction.atomic():
                Produto.objects.create(Produto='Calma Calabreso', preco=1.99)
                Produto.objects.create(Produto='Amostradinho', preco=20.0)
        except IntegrityError as e:
            print(f"Erro: {e}")
        
        self.client = Client()
        
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Calma Calabreso')
        self.assertContains(response, 'Amostradinho')
        print('Tudo certo na home👍')
        
            