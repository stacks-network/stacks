# -*- coding: utf-8 -*-
"""
    OpenName
    ~~~~~

    :copyright: (c) 2014 by The OpenName project
    :license: MIT, see LICENSE for more details.
"""

VALUE_MAX_LIMIT = 512

import json


#-----------------------------------
def utf8len(s):

    if type(s) == unicode:
        return len(s)
    else:
        return len(s.encode('utf-8'))


#-----------------------------------
def slice_profile(username, profile):

    keys = []
    values = []

    key = 'u/' + username.lower()
    keys.append(key)

    def max_size(username):
        return VALUE_MAX_LIMIT - len('next: i-' + username + '000000')

    #-----------------------------------
    def splitter(remaining, username):

        split = {}

        if utf8len(json.dumps(remaining)) < max_size(username):
            return remaining, None
        else:
            for key in remaining.keys():
                split[key] = remaining[key]

                if utf8len(json.dumps(split)) < max_size(username):
                    del remaining[key]
                else:
                    del split[key]
                    break
            return split, remaining

    #-----------------------------------
    def get_key(key_counter):
        return 'i/' + username.lower() + '-' + str(key_counter)

    split, remaining = splitter(profile, username)
    values.append(split)

    key_counter = 0
    counter = 0

    while(remaining is not None):

        key_counter += 1
        key = get_key(key_counter)

        split, remaining = splitter(remaining, username)
        keys.append(key)
        values.append(split)

        values[counter]['next'] = key
        counter += 1

    return keys, values
