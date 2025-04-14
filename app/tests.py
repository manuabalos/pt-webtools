from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app.models import SurveyResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class SurveyResponseTests(TestCase):
    def setUp(self):
        # Se crea un usuario de prueba.
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Se crea un token para el usuario.
        self.token = Token.objects.create(user=self.user)
        # Se crea un cliente API.
        self.client = APIClient()
        # Se configura el cliente API para usar autenticación por token.
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        # Se crea algunos datos de prueba.
        self.valid_payload = {
            'data': {'pregunta_1': 'Respuesta A', 'pregunta_2': 'Respuesta B'},
            'contact_email': 'testuser@example.com'
        }
        self.invalid_payload = {
            'data': {},
            'contact_email': 'invalid-email'
        }
    
    # Prueba validación de datos correctos.
    def test_create_valid_response(self):
        response = self.client.post(
            reverse('response-list'),
            self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    # Prueba validación de datos incorrectos.
    def test_create_invalid_response(self):
        response = self.client.post(
            reverse('response-list'),
            self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # Prueba de creación y obtención de datos de una respuesta.
    def test_get_all_responses(self):
        # Se crean las respuestas de prueba.
        SurveyResponse.objects.create(data={'q1': 'a1'}, contact_email='test1@example.com')
        SurveyResponse.objects.create(data={'q2': 'a2'}, contact_email='test2@example.com')
        
        # Seo obtienen todas las respuestas.
        response = self.client.get(reverse('response-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data['results']) == 2)