#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='grandcentral-py',
    version='0.0.1',
    description="GrandCentral is an extremely basic publisher subscriber event library",
    long_description=readme + '\n\n' + history,
    author="Ritesh Kadmawala",
    author_email='k.g.ritesh@gmail.com',
    url='https://github.com/kgritesh/grandcentral',
    packages=[
        'grandcentral',
    ],
    package_dir={'grandcentral':
                 'grandcentral'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='grandcentral',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
