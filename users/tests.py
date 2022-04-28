# from django.urls import reverse
# from requests import Response
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth import authenticate
# from .models import User
#
#
# class RegisterTestCase(APITestCase):
#
#     def test_register(self):
#         user_data = {'username': 'test',
#                      'email': 'test@gmail.com',
#                      'password': 'test2000'}
#         response = self.client.post('/api/v1/users/register/', user_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         print(list(response))


# class LoginTestCase(APITestCase):

# def test_login(self):
#     user_data = {'email': 'test@gmail.com',
#                  'password': 'test2000'}
#     user = authenticate(email=user_data["email"], password=user_data["password"])
#     response = self.client.post('/api/v1/users/login/', user)
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     print(list(response))

# def test_bad_login(self):
#     user_data = {'email': 'test@gmail.com',
#                  'password': 'test2000'}
#     user = authenticate(email=user_data["email"], password=user_data["password"])
#     response = self.client.post('/api/v1/users/login/', user)
#     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#     print(list(response))
