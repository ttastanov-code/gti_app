from django import forms
from tinymce.widgets import TinyMCE
from .models import Article


class ArticleForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={"cols": 80, "rows": 30}),
        label="Содержимое статьи"
    )

    seo_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        label="SEO Description",
        required=False
    )

    class Meta:
        model = Article
        fields = [
            "title",
            "image",
            "content",
            "is_published",

            # SEO
            "seo_title",
            "seo_description",
            "seo_keywords",
        ]
        widgets = {
            "seo_keywords": forms.TextInput(
                attrs={"placeholder": "ключевые слова через запятую"}
            ),
        }
