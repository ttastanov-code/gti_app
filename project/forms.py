# project/forms.py
from django import forms
from tinymce.widgets import TinyMCE
from .models import Project

class ProjectForm(forms.ModelForm):
    description = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 20}),
        label="Описание проекта"
    )

    class Meta:
        model = Project
        fields = ['name', 'image', 'description']
