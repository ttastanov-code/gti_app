from django.test import TestCase
from article.models import Article

class ArticleModelTest(TestCase):
    def test_article_str(self):
        article = Article.objects.create(
            title="Test Article",
            content="Content",
            image="test.jpg"
        )
        self.assertEqual(str(article), "Test Article")

    def test_default_is_published(self):
        article = Article.objects.create(
            title="Test",
            content="Text",
            image="test.jpg"
        )
        self.assertTrue(article.is_published)
