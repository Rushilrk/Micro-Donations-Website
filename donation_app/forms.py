'''
REFERENCES
  Title: Build A Blog Comment Section - Django Blog #33
  Author: Codemy.com
  Date: July 16, 2020
  Code version: Python 3.0 or later, HTML
  URL: https://www.youtube.com/watch?v=hZrlh4qU4eQ&ab_channel=Codemy.com
  Software License: BSD-3

  Title: Creating Comments System With Django
  Author: Django Central
  Date: September 2020
  Code version: Python 3.0 or later, HTML
  URL: https://djangocentral.com/creating-comments-system-with-django/
  Software License: BSD-3

  Title: Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture
  Author: Corey Schafer
  Date: August 31, 2018
  Code version: Python 3.0 or later, HTML
  URL: https://www.youtube.com/watch?v=FdVuKt_iuSI&ab_channel=CoreySchafer
  Software License: BSD-3, open source HPND License

  Title: Working with Forms
  Author: Django (Documentation)
  Date: September 2020
  Code version: Python 3.0 or later, HTML
  URL: https://docs.djangoproject.com/en/3.1/topics/forms/
  Software License: BSD-3

  Title: Writing your first Django app
  Author: Django (Documentation)
  Date: September 2020
  Code version: Python 3.0 or later, HTML
  URL: https://docs.djangoproject.com/en/3.1/intro/tutorial01/ and the rest of the tutorial in the link
  Software License: BSD-3
'''
from .models import Donation, Volunteer, Profile
from django import forms


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ['creator']
        fields = ('title', 'description', 'external_link', 'contact_info', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        exclude = ['creator']
        fields = ('title', 'description', 'external_link', 'contact_info', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }


class UpdateDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('title', 'description', 'external_link', 'contact_info')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }


class UpdateVolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('title',  'description', 'external_link', 'contact_info')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }


class MakeProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MakeProfile, self).__init__(*args, **kwargs)
    class Meta:
        model = Profile
        exclude = ['user']
        fields = ('image', 'bio', 'contact_info')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }


class ProfileUpdate(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('image', 'bio', 'contact_info')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }
