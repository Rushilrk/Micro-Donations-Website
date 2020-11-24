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
from django.contrib import admin
from .models import Donation, Volunteer, Profile

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'external_link', 'contact_info', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'external_link', 'contact_info', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'contact_info')

admin.site.register(Donation, DonationAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Profile, ProfileAdmin)