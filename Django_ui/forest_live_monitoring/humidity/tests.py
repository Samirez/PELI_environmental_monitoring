from django.test import TestCase

class HumidityTest(TestCase):
    """ Tests for the application views """
    def test_humidity(self):
        """ Test the humidity view """
        url = '/humidity/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Humidity')
        self.assertTemplateUsed(response, 'humidity/humidity.html')

    def test_humidity_data(self):
        """ Test the humidity data view """
        url = '/humidity/data/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Humidity')
        self.assertTemplateUsed(response, 'humidity/humidity_data.html')