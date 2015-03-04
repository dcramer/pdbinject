#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pdbinject',
    version='0.2.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/pdbinject',
    packages=find_packages(exclude=['example']),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pdbinject = pdbinject.runner:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
