#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import abspath, dirname, join, normpath
import sys

import dj_twiml

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = dj_twiml.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='dj-twiml',
    version=version,
    description="""Create Twilio TwiML views in Django""",
    long_description=open(
        normpath(join(dirname(abspath(__file__)), 'README.rst'))
    ).read(),
    author='Paul Hallett',
    author_email='paul@twilio.com',
    url='https://github.com/phalt/dj-twiml',
    packages=[
        'dj_twiml',
    ],
    include_package_data=True,
    install_requires=[
        'django_twilio',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django, twilio, twiml, telephony',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
