from django.test import TestCase, SimpleTestCase, Client
from .models import Donation, Volunteer, Profile
from django.contrib.auth.models import User
from .forms import DonationForm, VolunteerForm, UpdateDonationForm, UpdateVolunteerForm
from django.urls import reverse, resolve
from .views import donation_make, volunteer_make, DonationList, VolunteerList, DonationDetails, VolunteerDetails, UpdateDonation, UpdateVolunteer, DeleteDonation, VolunteerDelete, profile_make, profile
# Create your tests here.
class DonationModelTest(TestCase):
    def setUp(self):
        user = User.objects.create()
        user.save()
        Donation.objects.create(title  = "Testing", creator=user,  updated_on = "11/16/2000", description="THIS IS A TEST", created_on="11/16/2000",external_link="",contact_info="",status=0)
    
    def test_str(self):
        bob = Donation.objects.get(title = "Testing")
        self.assertEquals(str(bob), "Testing", "Does _str function work_")
        
    def test_get_absolute_url(self):
        bob = Donation.objects.get(title = "Testing")
        self.assertEquals(bob.get_absolute_url(), '/donation/list', "Does url return properly")

class VolunteerModelTest(TestCase):
    def setUp(self):
        user = User.objects.create()
        user.save()
        Volunteer.objects.create(title  = "Testing", creator=user,  updated_on = "11/16/2000", description="THIS IS A TEST", created_on="11/16/2000",external_link="",contact_info="",status=0)
    
    def test_str(self):
        bob = Volunteer.objects.get(title = "Testing")
        self.assertEquals(str(bob), "Testing", "Does _str function work_")
        
    def test_get_absolute_url(self):
        bob = Volunteer.objects.get(title = "Testing")
        self.assertEquals(bob.get_absolute_url(), '/volunteer/list', "Does url return properly")

class ProfileModelTest(TestCase):
    def setUp(self):
        b = User.objects.create(username = "testing")
        b.save()
        Profile.objects.create(user = b, bio = 'potato')
    def test_str(self):
        bob = Profile.objects.get(bio= 'potato')
        self.assertEquals(str(bob), f'testing Profile', "Does _str function work_")  
class TestForms(TestCase):
    
    #This tests that a valid request succeeds
    def test_donation_form(self):
        response = self.client.post('/donation/', {'title' : 'Test', 'slug' : 'something', 'description' : 'Abracadabra', 'external_link': 'abc.com', 'contact_info': '70303213' })
        self.assertEqual(response.status_code, 200)
        
    def test_volunteer_form(self):
        response = self.client.post('/volunteer/', {'title' : 'Test', 'slug' : 'something', 'description' : 'Abracadabra', 'external_link': 'abc.com', 'contact_info': '70303213' })
        self.assertEqual(response.status_code, 200)
    #update forms should be generated, but not available to a random user
    def test_update_volunteer_form(self):
        c = Client()
        response = c.post('/volunteer/', {'title' : 'Test', 'slug' : 'something', 'description' : 'Abracadabra', 'external_link': 'abc.com', 'contact_info': '70303213' })
        response2 = c.post('/volunteer/something/', {'title' : 'Test', 'slug' : 'something', 'description' : 'Abracadabra', 'external_link': 'abc.com', 'contact_info': '70303213' })
        self.assertEqual(response2.status_code, 405)
        
    def test_update_donation_form(self):
        c = Client()
        response = c.post('/donation/', {'title' : 'Test', 'slug' : 'something', 'description' : 'Abracadabra', 'external_link': 'abc.com', 'contact_info': '70303213' })
        response2 = c.post('/donation/something/', {'title' : 'Test', 'slug' : 'something', 'description' : 'Abracadabra', 'external_link': 'abc.com', 'contact_info': '70303213' })
        self.assertEqual(response2.status_code, 405)
        
   ## def test_profile_form(self):
    #     user = User.objects.create(username='testuser')
    #     user.set_password('12345')
     #   user.save()
    #    c = Client()
    #    logged_in = c.login(username='testuser', password='12345')
       # response1 = c.post('/profile/make/', {'bio' : 'something', 'contactinfo' : 'Abracadabra'})
    #    response = c.get('/profile/view/')
   #     self.assertEqual(response.status_code, 200)
        
class LoginTest(TestCase):
    def test_login(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertEqual(logged_in, 1, "logging in works")
        
    def test_login_wrongpassword(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12346')
        self.assertEqual(logged_in, 0, "logging in works")

    def test_login_wronguser(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testusers', password='12346')
        self.assertEqual(logged_in, 0, "logging in works")
"""
Checks all URLS Are Linked Properly
"""
class TestUrls(SimpleTestCase):
    def test_create_donation_works(self):
        url = reverse('donation_make')
        self.assertEquals(resolve(url).func, donation_make)

    def test_create_volunteer_works(self):
        url = reverse('volunteer_make')
        self.assertEquals(resolve(url).func, volunteer_make)

    def test_create_volunteer_not_work(self):
        url = reverse('volunteer_make')
        self.assertNotEquals(resolve(url).func, donation_make)

    def test_donation_list_works(self):
        url = reverse('donation', args=[])
        self.assertEquals(resolve(url).func.view_class, DonationList)

    def test_volunteer_list_works(self):
        url = reverse('volunteer', args=[])
        self.assertEquals(resolve(url).func.view_class, VolunteerList)

    def test_donation_details_works(self):
        url = reverse('donation_detail', args=['web-slug'])
        self.assertEquals(resolve(url).func.view_class, DonationDetails)

    def test_volunteer_details_works(self):
        url = reverse('volunteer_detail', args=['web-slug'])

        self.assertEquals(resolve(url).func.view_class, VolunteerDetails)

    def test_donation_update_works(self):
        url = reverse('update_donation', args=['web-slug'])
        self.assertEquals(resolve(url).func.view_class, UpdateDonation)

    def test_volunteer_update_works(self):
        url = reverse('update_volunteer', args=['web-slug'])
        self.assertEquals(resolve(url).func.view_class, UpdateVolunteer)

    def test_delete_donation_works(self):
        url = reverse('delete_donation', args=['web-slug'])
        self.assertEquals(resolve(url).func.view_class, DeleteDonation)

    def test_delete_volunteer_works(self):
        url = reverse('delete_volunteer', args=['web-slug'])
        self.assertEquals(resolve(url).func.view_class, VolunteerDelete)

    def test_delete_volunteer__not_works(self):
        url = reverse('delete_volunteer', args=['web-slug'])
        self.assertNotEquals(resolve(url).func.view_class, DonationList)

    def test_profile_make_works(self):
        url = reverse('profile_make', args=[])
        self.assertEquals(resolve(url).func, profile_make)
    
    def test_profile_works(self):
        url = reverse('profile', args=[])
        self.assertEquals(resolve(url).func, profile)


"""
Check to see if all the views use the correct template and makes sure the page is valid
"""
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.donation_form = reverse('donation_make')
        self.volunteer_form = reverse('volunteer_make')
        self.donation_list = reverse('donation', args=[])
        self.volunteer_list = reverse('volunteer', args=[])
        self.donation_detail = reverse('donation_detail', args=['web-slug'])

    def test_donation_make(self):
        response = self.client.get(self.donation_form)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donation_app/donate_form.html')

    def test_volunteer_make(self):
        response = self.client.get(self.volunteer_form)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donation_app/volunteer_form.html')

    def test_donation_list(self):
        response = self.client.get(self.donation_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donation_app/donation.html')

    def test_volunteer_list(self):
        response = self.client.get(self.volunteer_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donation_app/volunteer.html')

