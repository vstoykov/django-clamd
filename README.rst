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


Configuration
-------------

You can configure how to connect to Clamd. Default values are: ::

    CLAMD_SOCKET = '/var/run/clamav/clamd.ctl'
    CLAMD_USE_TCP = False
    CLAMD_TCP_SOCKET = 3310
    CLAMD_TCP_ADDR = '127.0.0.1'


You also can disable virus scanning for development with: ::

    CLAMD_ENABLED = False


Note: This is primary for make it easy running a project on development without
the need of installing Clamd on devlopment machine.


License
-------
`django-clamd` is released as open-source software under the LGPL license.
