from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Snippet


class DummieTests(TestCase):
    def test_list_snippet(self):
        self.assertTrue(True)


class SnippetsTests(APITestCase):
    def test_list_snippets(self):
        url = reverse('snippet-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Snippet.objects.count() >= 0)
