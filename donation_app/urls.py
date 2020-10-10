from . import views
from django.urls import path

urlpatterns = [
    path('', views.DonationList.as_view(), name='home'),
    path('<slug:slug>/', views.DonationDetails.as_view(), name='donation_detail'),
]