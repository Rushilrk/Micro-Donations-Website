from .models import Donation, Volunteer, Profile
from django import forms


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('title', 'description', 'creator', 'external_link', 'contact_info', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),

           # 'creator': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('title', 'description', 'creator', 'external_link', 'contact_info', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
           # 'creator': forms.TextInput(attrs={'class': 'form-control'}),
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
    class Meta:
        model = Profile
        fields = ('user', 'image', 'bio', 'contact_info')
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
