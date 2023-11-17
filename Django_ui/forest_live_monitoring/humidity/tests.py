from django.test import TestCase
from django.urls import reverse
import humidity.views
from django.contrib import admin


class Admin_test(TestCase):
    """ Tests for the application views """
    def admin_test(self):
        """ Test the admin view """
        response = self.client.get(reverse('admin'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'admin')
        self.assertTemplateUsed(response, admin.site.urls)

class HumidityTest(TestCase):
    """ Tests for the application views """
    def humidity_test(self):
        """ Test the humidity view """
        response = self.client.get(reverse('humidity'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'latest_readings')
        self.assertTemplateUsed(response, 'home.html')
