from django.shortcuts import render,HttpResponseRedirect, redirect
from .models import Donation, Volunteer, Profile
from django.views import generic
from .forms import DonationForm, VolunteerForm, UpdateDonationForm, UpdateVolunteerForm, ProfileUpdate, MakeProfile
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def donation_make(request):
    if request.method == "POST":
        donate = DonationForm(request.POST)
        if donate.is_valid():
            don = donate.save(commit=False)
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
            vol.save()
            return HttpResponseRedirect('list')
    else:
        volunteer = VolunteerForm()
    return render(request, 'donation_app/volunteer_form.html', {'form': volunteer})


class DonationList(generic.ListView):
    queryset = Donation.objects.filter(status=1).order_by('-created_on')
    template_name = 'donation_app/donation.html'


class DonationDetails(generic.DetailView):
    model = Donation
    template_name = 'donation_app/donation_detail.html'


class VolunteerList(generic.ListView):
    queryset = Volunteer.objects.filter(status=1).order_by('-created_on')
    template_name = 'donation_app/volunteer.html'


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
        prof = MakeProfile(request.POST, request.FILES)
        if prof.is_valid():
            pf = prof.save(commit=False)
            pf.save()
            return HttpResponseRedirect('view')
    else:
        prof = MakeProfile()
    return render(request, 'donation_app/profile_form.html', {'form': prof})


#@login_required
def profile(request):
    if request.method == "POST":
        form_class = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if form_class.is_valid():
            form_class.save()
        return redirect('profile')
    else:
        form_class = ProfileUpdate(instance=request.user.profile)
    context = {
        'form': form_class
    }
    return render(request, 'donation_app/profile.html', context)


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')