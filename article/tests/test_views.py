from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from article.models import Article

class ArticleListViewTest(TestCase):
    def setUp(self):
        Article.objects.create(
            title="Public",
            content="Text",
            image="a.jpg",
            is_published=True
        )
        Article.objects.create(
            title="Hidden",
            content="Text",
            image="b.jpg",
            is_published=False
        )

    def test_only_published_articles_displayed(self):
        response = self.client.get(reverse("article:list"))
        self.assertContains(response, "Public")
        self.assertNotContains(response, "Hidden")


class ArticleDetailViewTest(TestCase):
    def test_unpublished_article_not_found(self):
        article = Article.objects.create(
            title="Hidden",
            content="Text",
            image="a.jpg",
            is_published=False
        )
        response = self.client.get(reverse("article:detail", args=[article.pk]))
        self.assertEqual(response.status_code, 404)


class ArticleCreateAuthTest(TestCase):
    def test_create_requires_login(self):
        response = self.client.get(reverse("article:create"))
        self.assertEqual(response.status_code, 302)  # редирект на логин
