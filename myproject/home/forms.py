from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PhoneNumber
from django.contrib.auth.models import  User

class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.save()
        phone_number = self.cleaned_data['phone_number']
        PhoneNumber.objects.create(user=user, phone_number=phone_number)
        return user

    
