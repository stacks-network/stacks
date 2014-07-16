# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages

setup(
    name='onsuserschema',
    version='0.1.0',
    url='https://github.com/opennamesystem/user-schema',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'warlock == 1.1.0',
        'usefulutils >= 0.1.0'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False, 
)
