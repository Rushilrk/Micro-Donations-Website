from django.contrib import admin
from .models import Donation

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Donation, DonationAdmin)
