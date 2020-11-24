"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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

  Title: In 5 mins: Set up Google login to sign up users on Django
  Author: Zoe Chew
  Date: July 2019
  Code version: Python 3.0 or later, HTML, Google Login API
  URL: https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5
  Software License: BSD-3, Google Open Source
  
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from donation_app import views

urlpatterns = [
    path('', views.latest_posts, name='main'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('donation_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)