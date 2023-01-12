from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class TestTranstale(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def test_get_translator(self):
        client = Client()
        response = client.get(reverse('translate'))
        assert response.status_code == 200

    def test_post_translator(self):
        client = Client()
        response = client.post(reverse('translate'), data={
            'from_translate': 'ru',
            'lang': 'hello'
        })
        assert response.status_code == 200