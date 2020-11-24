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

  Title: Managing static files (e.g. images, JavaScript, CSS)
  Author: Django (Documentation)
  Date: October 2020
  Code version: Python 3.0 or later, HTML
  URL: https://docs.djangoproject.com/en/3.1/howto/static-files/
  Software License: BSD-3, open source HPND License

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
from django.shortcuts import render,HttpResponseRedirect, redirect
from .models import Donation, Volunteer, Profile
from django.views import generic
from .forms import DonationForm, VolunteerForm, UpdateDonationForm, UpdateVolunteerForm, MakeProfile, ProfileUpdate
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .filters import DonationFilter, VolunteerFilter
# Create your views here.


def latest_posts(request):
    don_posts = Donation.objects.filter(status=True).order_by('updated_on').reverse()[0:3]
    vol_posts = Volunteer.objects.filter(status=True).order_by('updated_on').reverse()[0:3]
    return render(request, 'donation_app/index.html', {'don_post': don_posts, 'vol_post': vol_posts})


def donation_make(request):
    if request.method == "POST":
        donate = DonationForm(request.POST)
        if donate.is_valid():
            don = donate.save(commit=False)
            don.creator = request.user
            don.save()
            return HttpResponseRedirect('list')
    else:
        donate = DonationForm()
    return render(request, 'donation_app/donate_form.html', {'form': donate})


def volunteer_make(request):
    if request.method == "POST":
        volunteer = VolunteerForm(request.POST)
        if volunteer.is_valid():
            vol = volunteer.save(commit=False)
            vol.creator = request.user
            vol.save()
            return HttpResponseRedirect('list')
    else:
        volunteer = VolunteerForm()
    return render(request, 'donation_app/volunteer_form.html', {'form': volunteer})


class DonationList(generic.ListView):
    model = Donation
    template_name = 'donation_app/donation.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DonationFilter(self.request.GET, queryset = self.get_queryset())
        return context

class DonationDetails(generic.DetailView):
    model = Donation
    template_name = 'donation_app/donation_detail.html'


class VolunteerList(generic.ListView):
    model = Volunteer
    template_name = 'donation_app/volunteer.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = VolunteerFilter(self.request.GET, queryset = self.get_queryset())
        return context


class VolunteerDetails(generic.DetailView):
    model = Volunteer
    template_name = 'donation_app/volunteer_detail.html'


class UpdateDonation(generic.UpdateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donation_app/update_donation.html'


class UpdateVolunteer(generic.UpdateView):
    model = Volunteer
    form_class = VolunteerForm
    template_name = 'donation_app/update_volunteer.html'

class DeleteDonation(generic.DeleteView):
    model = Donation
    template_name = 'donation_app/delete_donation.html'
    success_url = reverse_lazy('donation')

class VolunteerDelete(generic.DeleteView):
    model = Volunteer
    template_name = 'donation_app/delete_volunteer.html'
    success_url = reverse_lazy('volunteer')

def profile_make(request):
    if request.method == "POST":
        prof = MakeProfile(request.POST, request.FILES, user = request.user)
        if prof.is_valid():
            pf = prof.save(commit=False)
            pf.user = request.user
            pf.save()
            return HttpResponseRedirect('view')
    else:
        prof = MakeProfile(user=request.user)
    return render(request, 'donation_app/profile_form.html', {'form': prof})


def profile(request):
    if request.method == "POST":
        form_class = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if form_class.is_valid():
            form_class.save()
        return redirect('profile')
    else:
        form_class = ProfileUpdate(instance=request.user.profile)
        don_posts = Donation.objects.filter(status=True).filter(creator=request.user)
        vol_posts = Volunteer.objects.filter(status=True).filter(creator=request.user)
        don_drafts = Donation.objects.filter(status=0).filter(creator=request.user)
        vol_drafts = Volunteer.objects.filter(status=0).filter(creator=request.user)
    context = {
        'form': form_class,
        'don_posts' : don_posts,
        'vol_posts' : vol_posts,
        'don_drafts' : don_drafts,
        'vol_drafts' : vol_drafts,
    }
    return render(request, 'donation_app/profile.html', context)

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
