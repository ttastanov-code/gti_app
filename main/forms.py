from django import forms
from tinymce.widgets import TinyMCE
from .models import HomeBlock

class HomeBlockForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 15}),
        label="Содержимое блока"
    )

    class Meta:
        model = HomeBlock
        fields = ['title', 'content', 'order', 'is_active']
