from django.test import TestCase

# Create your tests here.
class HumidityTest(TestCase):
    """ Tests for the application views """
    def test_humidity(self):
        """ Test the humidity view """
        response = self.client.get('/humidity/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Humidity')
        self.assertTemplateUsed(response, 'humidity/humidity.html')
        