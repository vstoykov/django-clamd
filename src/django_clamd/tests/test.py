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
from django_clamd.validators import validate_file_infection
from .forms import UploadForm


class VirusValidatorTestCase(TestCase):
    def test_has_virus(self):
        infected_file = SimpleUploadedFile('eicar.txt', clamd.EICAR)
        form = UploadForm(files={'upload_file': infected_file})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'upload_file': ['File is infected with malware.']
        })

    def test_has_not_virus(self):
        uploaded_file = SimpleUploadedFile('some file.txt', b'File without viruses')
        form = UploadForm(files={'upload_file': uploaded_file})

        self.assertTrue(form.is_valid())

    def test_infinite_stream(self):

        class InfiniteStream:
            _read_bytes = 0
            _pos = 0

            def read(self, size):
                self._pos += size
                self._read_bytes += size
                return b'A' * size

            def seek(self, pos):
                self._pos = pos

            def tell(self):
                return self._pos

        stream = InfiniteStream()

        validate_file_infection(stream)
        self.assertGreaterEqual(stream._read_bytes, 5 * 1024 * 1024)
        self.assertEqual(stream.tell(), 0)
