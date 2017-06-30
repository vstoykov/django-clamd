#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.rst') as readme:
    readme = readme.read()

setup(
    name="django-clamd",
    version='0.4.0',
    author="Venelin Stoykov",
    author_email="vkstoykov@gmail.com",
    maintainer="Venelin Stoykov",
    maintainer_email="vkstoykov@gmail.com",
    keywords="python, django, clamav, antivirus, scanner, virus, libclamav, clamd",
    description="django-clamd is a django integration with Clamd (Clamav daemon).",
    long_description=readme,
    url="https://github.com/vstoykov/django-clamd",
    download_url="https://github.com/vstoykov/django-clamd/releases",
    bugtrack_url="https://github.com/vstoykov/django-clamd/issues",
    package_dir={'': 'src'},
    packages=find_packages('src', exclude="tests"),
    package_data={'django_clamd': [
        'locale/*/LC_MESSAGES/*.po',
        'locale/*/LC_MESSAGES/*.mo',
    ]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
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
