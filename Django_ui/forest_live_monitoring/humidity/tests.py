from django.test import TestCase
from django.urls import reverse
import humidity.views

class HumidityTest(TestCase):
    """ Tests for the application views """
    def test_humdity(self):
        """ Test the humidity view """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, '')
    


