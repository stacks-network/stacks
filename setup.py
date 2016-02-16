#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Blockstack:

    This installs blockstack-server and blockstack-client (cli)
    which are distributed under a GPLv3 license.
"""

from setuptools import setup, find_packages
import sys
import os

setup(
    name='blockstack',
    version='0.0.10.2',
    url='https://github.com/blockstack/blockstack',
    license='GPLv3',
    author='Blockstack.org',
    author_email='support@blockstack.org',
    description='Decentralized DNS for blockchain applications',
    keywords='blockchain bitcoin btc cryptocurrency name domain naming system data',
    download_url='https://github.com/blockstack/blockstack/archive/master.zip',
    zip_safe=False,
    install_requires=[
        'blockstore-client==0.0.12.2',
        'blockstore==0.0.10.2',
        'registrar==0.0.3'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
