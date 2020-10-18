from . import views
from django.urls import path

urlpatterns = [
    path('donation/', views.donation_make, name='donation_make'),
    path('volunteer/', views.volunteer_make, name='volunteer_make'),
    path('donation/list', views.DonationList.as_view(), name='donation'),
    path('volunteer/list', views.VolunteerList.as_view(), name='volunteer'),
    path('donation/<slug:slug>/', views.DonationDetails.as_view(), name='donation_detail'),
    path('volunteer/<slug:slug>/', views.VolunteerDetails.as_view(), name='volunteer_detail'),
    path('donation/update/<slug:slug>/', views.UpdateDonation.as_view(), name='update_donation'),
    path('volunteer/update/<slug:slug>/', views.UpdateVolunteer.as_view(), name='update_volunteer'),
    path('donation/delete/<slug:slug>/', views.DeleteDonation.as_view(), name='delete_donation'),
    path('volunteer/delete/<slug:slug>/', views.VolunteerDonation.as_view(), name='delete_volunteer'),
]