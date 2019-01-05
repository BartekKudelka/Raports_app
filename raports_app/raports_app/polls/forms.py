from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',)
        widgets = {
            'username',
            'email',
            'password1',
        }