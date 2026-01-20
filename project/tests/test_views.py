from django.test import TestCase
from django.urls import reverse
from project.models import Project

class ProjectViewsTest(TestCase):
    def test_project_list(self):
        Project.objects.create(
            name="Test Project",
            image="a.jpg",
            description="Desc"
        )

        response = self.client.get(reverse("project:list"))
        self.assertContains(response, "Test Project")
