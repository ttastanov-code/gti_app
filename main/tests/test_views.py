from django.test import TestCase
from django.urls import reverse
from main.models import HomeBlock

class HomeViewTest(TestCase):
    def test_home_page_status(self):
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 200)

    def test_only_active_blocks_displayed(self):
        HomeBlock.objects.create(title="Active", content="A", is_active=True)
        HomeBlock.objects.create(title="Hidden", content="B", is_active=False)

        response = self.client.get(reverse("main:home"))
        self.assertContains(response, "Active")
        self.assertNotContains(response, "Hidden")
