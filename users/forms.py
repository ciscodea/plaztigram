
# Django imports
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    # Sign up Form.
    username = forms.CharField(max_length=50, min_length=4)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput)
   
    first_name = forms.CharField(max_length=50, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
   
    email = forms.CharField(max_length=70, min_length=6, widget=forms.EmailInput)

    def clean_username(self):
        # usernamemust be unique.
        username = self.cleaned_data['username']
        query = User.objects.filter(username=username).exists()

        if query:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        # verify password confirmation match

        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password does not match')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

