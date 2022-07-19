from dataclasses import field, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Profile

from django.forms.widgets import ClearableFileInput


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'phone', 'profile_image', 'profession','short_intro', 'website_link',]

    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['readonly'] = True

        # self.fields['profile_image'].widget.clear_checkbox_label = "clear"
        # self.fields['profile_image'].widget.initial_text = " "
        # self.fields['profile_image'].widget.input_text = " "
        # self.fields['profile_image'].widget.template_name

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
