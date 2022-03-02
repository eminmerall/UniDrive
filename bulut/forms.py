from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username = forms.CharField(max_length=100, label="kullanıcı adı")
    password = forms.CharField(max_length=100, label="parola", widget=forms.PasswordInput)

class registerForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email'
        ]
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolalar eşleşmiyor")
        return password2

