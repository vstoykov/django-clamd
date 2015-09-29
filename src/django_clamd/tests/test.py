import os
import clamd

# Ensure we can import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_clamd.tests.settings'

import django
if hasattr(django, 'setup'):
    # Django >= 1.7
    django.setup()

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import UploadForm


class AnimalTestCase(TestCase):
    def test_virus_validator(self):
        infected_file = SimpleUploadedFile('eicar.txt', clamd.EICAR)
        form = UploadForm(files={'upload_file': infected_file})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'upload_file': ['File is infected with mallware']
        })
