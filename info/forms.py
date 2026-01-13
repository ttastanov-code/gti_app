# info/forms.py
from django import forms
from tinymce.widgets import TinyMCE
from .models import Page, Vacancy

class PageForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 20}),
        label="Содержимое страницы"
    )

    class Meta:
        model = Page
        fields = ['page_type', 'title', 'content', 'is_active']


class VacancyForm(forms.ModelForm):
    description = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 15}),
        label="Описание вакансии"
    )
    requirements = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 10}),
        label="Требования",
        required=False
    )
    responsibilities = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 10}),
        label="Обязанности",
        required=False
    )

    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'requirements', 'responsibilities', 'is_active']