from django.test import TestCase
from django.urls import reverse
from info.models import Vacancy, Page

class VacancyListTest(TestCase):
    def setUp(self):
        Vacancy.objects.create(title="Active", description="D", is_active=True)
        Vacancy.objects.create(title="Hidden", description="D", is_active=False)

    def test_only_active_vacancies(self):
        response = self.client.get(reverse("info:vacancy_list"))
        self.assertContains(response, "Active")
        self.assertNotContains(response, "Hidden")


class PageDetailTest(TestCase):
    def test_page_by_type(self):
        Page.objects.create(
            page_type="about",
            title="About",
            content="Text",
            is_active=True
        )

        response = self.client.get(reverse("info:page", args=["about"]))
        self.assertContains(response, "About")
