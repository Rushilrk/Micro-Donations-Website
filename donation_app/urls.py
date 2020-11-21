from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account/logout/', views.Logout, name='logout'),
    path('donation/', views.donation_make, name='donation_make'),
    path('volunteer/', views.volunteer_make, name='volunteer_make'),
    path('profile/view', views.profile, name='profile'),
    path('profile/make', views.profile_make, name='profile_make'),
    path('donation/account/logout', views.Logout),
    path('volunteer/account/logout', views.Logout),
    path('profile/account/logout', views.Logout),
    path('donation/list', views.DonationList.as_view(), name='donation'),
    path('volunteer/list', views.VolunteerList.as_view(), name='volunteer'),
    path('donation/<slug:slug>/', views.DonationDetails.as_view(), name='donation_detail'),
    path('volunteer/<slug:slug>/', views.VolunteerDetails.as_view(), name='volunteer_detail'),
    path('donation/update/<slug:slug>/', views.UpdateDonation.as_view(), name='update_donation'),
    path('volunteer/update/<slug:slug>/', views.UpdateVolunteer.as_view(), name='update_volunteer'),
    path('donation/delete/<slug:slug>/', views.DeleteDonation.as_view(), name='delete_donation'),
    path('volunteer/delete/<slug:slug>/', views.VolunteerDelete.as_view(), name='delete_volunteer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)