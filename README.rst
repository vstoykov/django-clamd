django-clamd
=============

This project integrates python-clamd with Django for easy scanning files for viruses on upload


Usage
-----

You can use it in forms::

    from django import forms
    from django_clamd.validators import validate_file_infection

    class UploadForm(forms.Form):
        upload_file = forms.FileField(validators=[validate_file_infection])


Or you can add it as validator directly in your model::

    from django.db import models
    from django_clamd.validators import validate_file_infection

    class FileModel(models.Model):
        document = models.FileField(validators=[validate_file_infection])


You will have automatically scanning of upladed files in Django Admin
and also when create ModelForm's for that model.
