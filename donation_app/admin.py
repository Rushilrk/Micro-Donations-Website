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