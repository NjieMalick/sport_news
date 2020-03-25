from django.test import TestCase


class PostTests(TestCase):
    def test_post_list_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_premierleague_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
