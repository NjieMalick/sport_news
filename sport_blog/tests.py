from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('england')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)