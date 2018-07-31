#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='datav',
    version='0.0.1',
    description='Data Analysis Tool and Visualizer',
    long_description=readme,
    author='nahid pervez',
    author_email='nahidpervez@gmail.com',
    url='https://github.com/nahidpervez/datv',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
