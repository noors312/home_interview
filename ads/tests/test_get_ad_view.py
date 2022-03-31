import unittest.mock

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.test import APITestCase

from ads.models import AdRequest


@unittest.mock.patch('requests.get')
class TestGetAdAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('get_ad')

    def test_api_returns_400_with_not_provided_username_or_sdk_version(self, requests_mock):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)

    def test_api_creates_ad_request(self, requests_mock):
        with open('ads/tests/fixtures/valid_response.xml', 'rb') as f:
            requests_mock.return_value = HttpResponse(f.read(), content_type='text/xml')

        response = self.client.get(self.url, data={'username': 'noors'})
        requests_mock.assert_called_once_with(settings.VAST_API_URL)
        self.assertEqual(AdRequest.objects.count(), 1)
        self.assertEqual(requests_mock.return_value.content, response.content)

    def test_api_returns_response_from_VAST_API_on_error(self, requests_mock):
        with open('ads/tests/fixtures/invalid_response.xml', 'rb') as f:
            requests_mock.return_value = HttpResponse(f.read(), content_type='text/xml')

        response = self.client.get(self.url, data={'username': 'noors'})
        requests_mock.assert_called_once_with(settings.VAST_API_URL)
        self.assertEqual(requests_mock.return_value.content, response.content)

    def test_api_calls_VAST_API(self, requests_mock):
        with open('ads/tests/fixtures/valid_response.xml', 'rb') as f:
            requests_mock.return_value = HttpResponse(f.read(), content_type='text/xml')

        response = self.client.get(self.url, data={'username': 'noors'})
        requests_mock.assert_called_once_with(settings.VAST_API_URL)
        self.assertEqual(requests_mock.return_value.content, response.content)
