#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2022 The American School of Barcelona
    :contact: fleon@asbarcelona.com
"""


from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(
    name='django4_bootstrap_breadcrumbs',
    version='0.10.0',
    url='https://github.com/fleonasb/django4-bootstrap-breadcrumbs',
    license='MIT',
    description='Django breadcrumbs for Bootstrap 2, 3 or 4',
    long_description='Django template tags used to generate breadcrumbs html '
                     'using bootstrap css classes or custom template',
    author='Fidel Leon',
    author_email='fleon@asbarcelona.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'six',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    zip_safe=False,
    include_package_data=True,
)
