"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from rest_framework.test import APIClient
from PIL import Image


# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            django.setup()

    def test_image_upload(self):
        client = APIClient()
        image = Image.new('RGB', (100, 100))

        tmp_file = "test.jpg"
        image.save(tmp_file)
        
        with open(tmp_file, 'rb') as data:
            responce = client.post('', {'image': data, 'name': "Max Kvt"}, format='multipart')

            print(responce)

        
