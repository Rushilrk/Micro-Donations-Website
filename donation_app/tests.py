from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from donation_app.views import donation_make, volunteer_make, DonationList, VolunteerList, DonationDetails, VolunteerDetails, UpdateDonation, UpdateVolunteer, DeleteDonation, VolunteerDelete
from .models import Donation, Volunteer

# Create your tests here.
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



class TestModels(TestCase):
    def setUp(self):
        self.donation1 = Donation.objects.create(
            title='Color Run',
            slug='color-run',
            description='This is a color run event',
            external_link='abcdefg.com',
            contact_info='123-456-7890',
            status=1
        )
        self.donation2 = Donation.objects.create(
            title='Salvation Army',
            slug='salvation_army',
            description='This is a salvation army event',
            external_link='abcdefg.com',
            contact_info='123-456-7890',
            status=0
        )

    def check_donation_is_published(self):
        self.assertEquals(self.donation1.status == 1)
        self.assertNotEquals(self.donation2.status == 1)
