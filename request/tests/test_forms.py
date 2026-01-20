from django.test import TestCase
from request.forms import RequestForm

class RequestFormTest(TestCase):
    def test_honeypot_spam_field(self):
        form = RequestForm(data={
            "name": "Bot",
            "email": "bot@test.com",
            "phone": "+77001234567",
            "message": "Spam",
            "website": "spam"
        })
        self.assertFalse(form.is_valid())
