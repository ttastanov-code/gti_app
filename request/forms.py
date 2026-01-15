from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    # honeypot поле (боты часто его заполняют)
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )

    class Meta:
        model = Request
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected")
        return ""
