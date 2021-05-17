from django import forms


class SmsForm(forms.Form):
    auto_code = forms.CharField(label='Code', help_text="enter code from sms")
