# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

import warlock
from usefulutils import to_dict

from .schema import user_schema

User = warlock.model_factory(user_schema)
User.to_dict = to_dict
