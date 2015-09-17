from django import forms
from django_clamd.validators import validate_file_infection


class UploadForm(forms.Form):
    upload_file = forms.FileField(validators=[validate_file_infection])
