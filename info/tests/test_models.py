from django.test import TestCase
from info.models import Page, Vacancy

class PageModelTest(TestCase):
    def test_str(self):
        page = Page.objects.create(
            page_type="about",
            title="About us",
            content="Text"
        )
        self.assertEqual(str(page), "About us")


class VacancyModelTest(TestCase):
    def test_str(self):
        vacancy = Vacancy.objects.create(
            title="Python Developer",
            description="Desc"
        )
        self.assertEqual(str(vacancy), "Python Developer")
