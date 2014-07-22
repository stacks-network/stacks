# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.1.0'

import warlock
from usefulutils import to_dict
from .userschema import userschema

User = warlock.model_factory(userschema)
User.to_dict = to_dict