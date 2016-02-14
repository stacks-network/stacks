# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages

setup(
    name='openspecs',
    version='0.1.3',
    url='https://github.com/opennamesystem/openspecs',
    description='Protocol specifications for the Open Name System',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'usefulutils == 0.1.2'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
