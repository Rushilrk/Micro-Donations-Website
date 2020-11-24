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
  
  Title: Unique Slugify
  Author: SmileyChris
  Date: April 8, 2008
  Code Version: Python
  URL: https://djangosnippets.org/snippets/690/
  
  Software License: None in particular
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
import re
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Donation(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    external_link = models.CharField(max_length=200, default='')
    contact_info = models.CharField(max_length=200, default='')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('donation')
    
    def save(self, **kwargs):
        if not self.id:
            slug_str = "%s %s" % (self.title, self.creator) 
            unique_slugify(self, slug_str) 
            
        super(Donation, self).save(**kwargs)

class Volunteer(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='volunteer')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    external_link = models.CharField(max_length=200, default='')
    contact_info = models.CharField(max_length=200, default='')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('volunteer')
    
    def save(self, **kwargs):
        if not self.id:
            slug_str = "%s %s" % (self.title, self.creator) 
            unique_slugify(self, slug_str) 
            
        super(Volunteer, self).save(**kwargs)
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pfp')
    bio = models.TextField(default='')
    contact_info = models.CharField(max_length=200, default='')
    def __str__(self):
        return f'{self.user.username} Profile'