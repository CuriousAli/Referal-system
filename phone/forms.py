from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class ReferalForm(forms.ModelForm):
    inv_ref = forms.CharField(label='Invite referal', help_text='Input referal code(noT Your own)')
    class Meta:
        model = User
        fields = ('inv_ref',)


class CustomRegForm(UserCreationForm):
    number = forms.CharField(label='Номер телефона')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')
    class Meta:
        model = User
        fields = ('number', 'password1', 'password2')