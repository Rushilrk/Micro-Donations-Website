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