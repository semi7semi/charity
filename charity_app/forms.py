from django import forms
from django.contrib.auth.models import User

class RegisterUserForm(forms.ModelForm):
    password_2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "password_2"]
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': 'Imię'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            "email": forms.TextInput(attrs={'placeholder': 'Email'}),
            "password": forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
            "password_2": forms.PasswordInput
        }
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": ""
        }


class LogForm(forms.Form):
    username = forms.CharField(max_length=64, label="", widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(max_length=64, label="", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
