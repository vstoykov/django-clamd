django-clamd
=============

This project integrates python-clamd with Django for easy scanning files for viruses on upload


Install
-------

From PyPi with pip:

.. code-block:: bash

    pip install django-clamd

or

.. code-block:: bash

    easy_install django-clamd

You can also install development version directly from GitHub:

.. code-block:: bash

    pip install git+https://github.com/vstoykov/django-clamd.git


Additionally if you want translations to work you need to add it to installed apps.

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_clamd',
        ...
    )
    
    
Additionally if you are using Ubuntu, in order for django-clamd to work install clamav-daemon.

.. code-block:: bash

    sudo apt-get install clamav-daemon


Usage
-----

You can use it in forms:

.. code-block:: python

    from django import forms
    from django_clamd.validators import validate_file_infection

    class UploadForm(forms.Form):
        upload_file = forms.FileField(validators=[validate_file_infection])


Or you can add it as validator directly in your model:

.. code-block:: python

    from django.db import models
    from django_clamd.validators import validate_file_infection

    class FileModel(models.Model):
        document = models.FileField(validators=[validate_file_infection])


You will have automatically scanning of upladed files in Django Admin
and also when create ModelForm's for that model.


Configuration
-------------

By default :code:`django-clamd` tries to be smart and with good defaults.
You can still configure how to connect to Clamd. Default values are:

.. code-block:: python

    CLAMD_SOCKET = '/var/run/clamav/clamd.ctl'
    CLAMD_USE_TCP = False
    CLAMD_TCP_SOCKET = 3310
    CLAMD_TCP_ADDR = '127.0.0.1'

Note: When you are running on Fedora or CentOS and :code:`clamav-scanner`
package is installed then default value for :code:`CLAMD_SOCKET` is:

.. code-block:: python

    CLAMD_SOCKET = '/var/run/clamd.scan/clamd.sock'

By default, this package will *allow* a file if ClamD cannot be contacted or
if the scan fails. If you want validation to fail in these instances, change
:code:`CLAMD_FAIL_BY_DEFAULT`

.. code-block:: python

    CLAMD_FAIL_BY_DEFAULT = True

You also can disable virus scanning for development with:

.. code-block:: python

    CLAMD_ENABLED = False

Note: This is primary for make it easy to run a project on development without
the need of installing Clamd on devlopment machine.


License
-------
`django-clamd` is released as open-source software under the LGPL license.
