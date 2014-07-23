# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

import unittest
from test import test_support

import json
from openspecs import userschema
from jsonschema import validate
from sample_json import sample_json

class UserSchemaTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_schema_with_example_userdata(self):
        for v in sample_json:
            validate(v, userschema.schema)

def test_main():
    test_support.run_unittest(
        UserSchemaTests,
    )

if __name__ == '__main__':
    test_main()

