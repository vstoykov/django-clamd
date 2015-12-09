#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.rst') as readme:
    readme = readme.read()

setup(
    name="django-clamd",
    version='0.3.0',
    author="Venelin Stoykov",
    author_email="vkstoykov@gmail.com",
    maintainer="Venelin Stoykov",
    maintainer_email="vkstoykov@gmail.com",
    keywords="python, django, clamav, antivirus, scanner, virus, libclamav, clamd",
    description="django-clamd is a django integration with Clamd (Clamav daemon).",
    long_description=readme,
    url="https://github.com/vstoykov/django-clamd",
    package_dir={'': 'src'},
    packages=find_packages('src', exclude="tests"),
    package_data={'django_clamd': [
        'locale/*/LC_MESSAGES/*.po',
        'locale/*/LC_MESSAGES/*.mo',
    ]},
    classifiers=[
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    ],
    install_requires=(
        "clamd",
        "Django>=1.4",
    ),
    tests_require=(
        "nose==1.3.7",
    ),
    test_suite='nose.collector',
    zip_safe=False,
    include_package_data=True,
)
