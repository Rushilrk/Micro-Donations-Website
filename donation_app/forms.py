from .models import Donation, Volunteer
from django import forms


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('title', 'slug', 'description', 'creator', 'external_link', 'contact_info', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
           # 'creator': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('title', 'slug', 'description', 'creator', 'external_link', 'contact_info', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
           # 'creator': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }


class UpdateDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('title', 'slug', 'description', 'external_link', 'contact_info')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }


class UpdateVolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('title', 'slug', 'description', 'external_link', 'contact_info')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'external_link': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'})
        }