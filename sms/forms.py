from django import forms
from .models import Sms_Code


class SmsForm(forms.ModelForm):
    auto_code = forms.CharField(label='Code', help_text="Enter code from sms")
    class Meta:
        model = Sms_Code
        fields = ('auto_code',)