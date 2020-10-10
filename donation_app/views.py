from django.shortcuts import render
from .models import Donation
from django.views import generic
# Create your views here.
class DonationList(generic.ListView):
    queryset = Donation.objects.filter(status=1).order_by('-created_on')
    template_name = 'donation_app/donation.html'

class DonationDetails(generic.DetailView):
    model = Donation
    template_name = 'donation_detail.html'