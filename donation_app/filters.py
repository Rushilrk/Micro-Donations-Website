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
  
  Title: Django Filtering System with django-filter - Filter Queryset (2018)
  Author: The Dumbfounds
  Date: Jun 23, 2018
  Code version: Python 3.0 or later, HTML
  URL: https://www.youtube.com/watch?v=nle3u6Ww6Xk
  Software License: N/A
  
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
