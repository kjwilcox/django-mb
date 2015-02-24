#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-mb',
    version='0.1',
    description='A simple message board written in Django',
    author='Kyle Wilcox',
    author_email='k.j.wilcox@gmail.com',
    packages=find_packages(exclude=('tests',)),
    install_requires=(
        'Django',
    )
)
