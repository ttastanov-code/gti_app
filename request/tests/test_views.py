from django.test import TestCase
from django.urls import reverse
from request.models import Request
from django.utils.timezone import now
from datetime import timedelta

class RequestFloodProtectionTest(TestCase):
    def test_flood_limit(self):
        url = reverse("request:form")

        for i in range(4):
            Request.objects.create(
                name="Test",
                email="a@test.com",
                phone="+77001234567",
                message="Hi"
            )

        response = self.client.post(url, {
            "name": "User",
            "email": "u@test.com",
            "phone": "+77001234567",
            "message": "Hello"
        })

        self.assertContains(response, "Слишком много запросов")
