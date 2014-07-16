# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

import unittest
from test import test_support

from onsuserschema import User, user_schema
from jsonschema import validate

example_user_json = {
    "basics": {
        "name": "Ryan Shea",
        "location": "New York, NY",
        "bio": "Co-founder of @OneNameio with @Muneeb. Bitcoin, identity, the blockchain, and decentralization."
    },
    "photos": [
        { "type": "avatar", "url": "https://s3.amazonaws.com/97p/tux.jpg" },
        { "type": "cover", "url": "https://s3.amazonaws.com/dx3/ryanshea" },
    ],
    "payments": [
        { "type": "bitcoin", "address": "14eautXfJT7EZsKfm1eHSAPnHkn3w1XF9R" },
    ],
    "profiles": [
        { "type": "twitter", "username": "ryaneshea", "proof": "https://twitter.com/ryaneshea/status/486057647808868352" },
        { "type": "github", "username": "rxl", "proof": "https://gist.github.com/rxl/9799732" },
    ],
    "websites": [
        { "label": "Blog", "url": "http://shea.io" },
    ],
    "pgp": {
        "url": "https://s3.amazonaws.com/97p/pubkey.asc",
        "fingerprint": "DDA1CF3D659064044EC99354429E1A42A93EA312",
    },
    "email": [
        { "address": "ryan@shea.io" }
    ],
    "v": "0.3",
}

class UserSchemaTests(unittest.TestCase):
    def setUp(self):
        self.example_user_json = example_user_json

    def tearDown(self):
        pass
        
    def test_warlock_user_object_with_example_userdata(self):
        user = User(**self.example_user_json)
        assert(user)

    def test_user_schema_with_example_userdata(self):
        validate(self.example_user_json, user_schema)

def test_main():
    test_support.run_unittest(
        UserSchemaTests,
    )

if __name__ == '__main__':
    test_main()

