from django import forms

# Models 
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.Form):
    
    username = forms.CharField(min_length=3, max_length=50)

    password = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.PasswordInput()
        )

    password_confirmation = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.PasswordInput()
        )

    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    email = forms.CharField(
        min_length=6, 
        max_length=50, 
        required=True, 
        widget=forms.EmailInput()
        )
    birth_date = forms.DateField()


    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Sorry, this username is already in us')
        return username

    
    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Sorry, the passwords do not match.')

        return data


    def save(self):
        data = self.cleaned_data
        birth_date = data['birth_date']
        data.pop('password_confirmation')
        data.pop('birth_date')

        user = User.objects.create_user(**data)
        profile = Profile(user=user, birth_date=birth_date)
        # import pdb; pdb.set_trace()
        profile.save()
