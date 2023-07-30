from django import forms
from django.contrib.auth.models import User
from main.models import Subscribe, CrossfitTraining


class RegisterForm(forms.Form):
    placeholders = {
        'first_name': 'First name',
        'last_name': 'Last name',
        'username': 'Username',
        'email': 'Email',
        'password1': 'Password',
        'password2': 'Confirm password',
    }
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': placeholders['first_name']}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': placeholders['last_name']}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': placeholders['username']}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': placeholders['email']}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': placeholders['password1']}))
    password2 = forms.CharField(label='Password Confirm',
                                widget=forms.PasswordInput(attrs={'placeholder': placeholders['password2']}))


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmailForm(forms.ModelForm):
    objects = None

    class Meta:
        model = Subscribe
        fields = '__all__'


class SearchForm(forms.Form):
    query = forms.CharField(label='Search Query', max_length=100)


class Services(forms.ModelForm):
    object = None

    class Meta:
        model = CrossfitTraining
        fields = '__all__'
