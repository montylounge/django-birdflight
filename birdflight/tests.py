from django.test.client import Client
import unittest


class BirdFlightTests(unittest.TestCase):

    def test_homepage(self):
        '''Test the homepage view.'''

        c = Client()
        response = c.get('/')
        self.failUnlessEqual(response.status_code, 200)






