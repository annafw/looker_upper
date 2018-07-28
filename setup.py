# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='looker_upper',
    version='0.1.0',
    description='Look up product ingredients',
    long_description=readme,
    author='Anna Winkler',
    author_email='me.anna.winkler@gmail.com',
    url='https://github.com/annawinkler/looker_upper',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

