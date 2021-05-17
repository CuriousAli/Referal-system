from django import forms
from .models import User

class ReferalForm(forms.ModelForm):
    inv_ref = forms.CharField(label='Invite referal', help_text='Input referal code(noT Your own)')
    class Meta:
        model = User
        fields = ('inv_ref',)