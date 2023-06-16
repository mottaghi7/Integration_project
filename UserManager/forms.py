from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    class Meta:
        models = get_user_model()
        fields = ['email', 'password']


class SignUpForm(forms.Form):
    class Meta:
        models = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class EmailSendForm(forms.Form):
    subject = forms.CharField(label='موضوع', max_length=100)
    message = forms.CharField(label='متن', max_length=1000)
    receivers = forms.CharField(label='گیرندگان', help_text='ایمیل گیرندگان با کاما از هم جدا شوند', max_length=1000)
