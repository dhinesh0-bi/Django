from django.test import TestCase
from django.urls import reverse

class StatusEndpointTests(TestCase):

    def test_status_endpoint(self):
        url = reverse("api-status")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json())
        self.assertIn("version", response.json())
        self.assertEqual(response.json()["status"], "ok")
