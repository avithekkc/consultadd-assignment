from django import forms
from django.core import validators


def validate(password):
    special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    if not any(char.isdigit() for char in password):
        raise forms.ValidationError('Password must contain at least 1 digit.')
    if not any(char.isalpha() for char in password):
        raise forms.ValidationError('Password must contain at 1 least  letter.')
    if not any(char in special_characters for char in password):
        raise forms.ValidationError('Password must contain at least 1 special character.')


class signupForm(forms.Form):
    name = forms.CharField(label="Enter Name", max_length=50)
    email = forms.EmailField(label="Enter Email", max_length=50)
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput, validators=[validate])

