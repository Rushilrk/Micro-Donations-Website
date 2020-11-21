from django.shortcuts import render,HttpResponseRedirect, redirect
from .models import Donation, Volunteer
from django.views import generic
from .forms import DonationForm, VolunteerForm, UpdateDonationForm, UpdateVolunteerForm, MakeProfile, ProfileUpdate
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .filters import DonationFilter, VolunteerFilter
# Create your views here.


def latest_posts(request):
    don_posts = Donation.objects.filter(status=True).order_by('updated_on')[0:3]
    vol_posts = Volunteer.objects.filter(status=True).order_by('updated_on')[0:3]
    return render(request, 'donation_app/index.html', {'don_post': don_posts, 'vol_post': vol_posts})


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
        prof = MakeProfile(request.POST, request.FILES)
        if prof.is_valid():
            pf = prof.save(commit=False)
            pf.save()
            return HttpResponseRedirect('view')
    else:
        prof = MakeProfile()
    return render(request, 'donation_app/profile_form.html', {'form': prof})


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
