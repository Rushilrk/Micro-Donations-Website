from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pfp')
    bio = models.TextField(default='')
    contact_info = models.CharField(max_length=200, default='')
    def __str__(self):
        return f'{self.user.username} Profile'