from django.urls import reverse
from rest_framework.test import APITestCase

from ads.tests.factories.ad_request import AdRequestFactory
from ads.tests.factories.impression import ImpressionFactory


class TestGetStatsAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("get_stats")

    def test_view_returns_correct_data(self):
        test_ad_requests = [AdRequestFactory() for _ in range(10)]
        test_impressions = [ImpressionFactory() for _ in range(5)]

        expected_data = {
            "ad_per_client": len(test_ad_requests),
            "impression_per_client": len(test_impressions),
            "fill_rate": round(len(test_impressions) / len(test_ad_requests), 2),
        }

        response = self.client.get(self.url)

        self.assertEqual(expected_data, response.json())

    def test_view_calculate_filtered_data(self):
        _ = [AdRequestFactory() for _ in range(5)]  # 5 requests with default username
        test_ad_requests = [AdRequestFactory(username="test") for _ in range(3)]
        test_impressions = [ImpressionFactory(username="test") for _ in range(5)]

        expected_data = {
            "ad_per_client": len(test_ad_requests),
            "impression_per_client": len(test_impressions),
            "fill_rate": round(len(test_impressions) / len(test_ad_requests), 2),
        }

        response = self.client.get(self.url, data={"username": "test"})
        self.assertEqual(expected_data, response.json())

    def test_view_returns_count_of_impression_if_ad_requests_count_is_zero(self):
        test_ad_requests = []
        test_impressions = [ImpressionFactory(username="test") for _ in range(5)]

        expected_data = {
            "ad_per_client": len(test_ad_requests),
            "impression_per_client": len(test_impressions),
            "fill_rate": round(len(test_impressions) / 1, 2),
        }

        response = self.client.get(self.url, data={"username": "test"})
        self.assertEqual(expected_data, response.json())
