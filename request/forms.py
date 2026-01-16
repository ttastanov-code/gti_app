from django import forms
from .models import Request


# request/forms.py
class RequestForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Request
        fields = ['name', 'email', 'phone', 'message', 'file']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected")
        return ""

    def clean_file(self):
        file = self.cleaned_data.get("file")
        if file:
            max_size = 50 * 1024 * 1024  # 50 MB
            if file.size > max_size:
                raise forms.ValidationError("Размер файла не должен превышать 50 МБ.")
        return file

