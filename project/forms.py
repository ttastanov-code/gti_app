from django import forms
from tinymce.widgets import TinyMCE
from .models import Project


class ProjectForm(forms.ModelForm):
    description = forms.CharField(
        widget=TinyMCE(attrs={"cols": 80, "rows": 20}),
        label="Описание проекта"
    )

    seo_description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        label="SEO Description",
        required=False
    )

    class Meta:
        model = Project
        fields = [
            "name",
            "image",
            "description",

            # SEO
            "seo_title",
            "seo_description",
            "seo_keywords",
        ]
        widgets = {
            "seo_keywords": forms.TextInput(
                attrs={"placeholder": "gti, проект, цифровые экраны, алматы"}
            ),
        }
