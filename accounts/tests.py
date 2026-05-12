from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser


class AccountTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='Manoel',
            password='SenhaCorreta@1234'
        )

    def test_cadastro_valido(self):
        response = self.client.post(reverse('register'), {
            'username': 'Cândido',
            'password1': 'SenhaCorreta@1234',
            'password2': 'SenhaCorreta@1234',
        })
        self.assertEqual(response.status_code, 302)

    def test_cadastro_invalido(self):
        response = self.client.post(reverse('register'), {
            'username': 'Cândido',
            'password1': 'SenhaCorreta@1234',
            'password2': 'SenhaIncorreta@1234',
        })
        self.assertEqual(response.status_code, 200)

    def test_login_valido(self):
        response = self.client.post(reverse('login'), {
            'username': 'Manoel',
            'password': 'SenhaCorreta@1234',
        })
        self.assertEqual(response.status_code, 302)

    def test_login_invalido(self):
        response = self.client.post(reverse('login'), {
            'username': 'Manoel',
            'password': 'SenhaIncorreta@1234',
        })
        self.assertEqual(response.status_code, 200)
