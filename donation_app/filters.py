import django_filters
from .models import Donation, Volunteer

class DonationFilter(django_filters.FilterSet):
    
    CHOICES = (
        ('ascending', 'Recent'),
        ('descending', 'Oldest'),
        )
    ordering = django_filters.ChoiceFilter(label = 'Ordering', choices = CHOICES, method='filter_by_date')
    class Meta:
        model = Donation
        fields = {'title' : ['icontains'], 'creator' : ['exact'],}
    def filter_by_date(self, queryset, name, value):
        expression = '-created_on' if value == 'ascending' else 'created_on'
        return queryset.order_by(expression)
    
class VolunteerFilter(django_filters.FilterSet):
    
    CHOICES = (
        ('ascending', 'Recent'),
        ('descending', 'Oldest'),
        )
    ordering = django_filters.ChoiceFilter(label = 'Ordering', choices = CHOICES, method='filter_by_date')
    class Meta:
        model = Volunteer
        fields = {'title' : ['icontains'], 'creator' : ['exact'],}
    def filter_by_date(self, queryset, name, value):
        expression = '-created_on' if value == 'ascending' else 'created_on'
        return queryset.order_by(expression)