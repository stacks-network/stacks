# -*- coding: utf-8 -*-
"""
    OpenName
    ~~~~~

    :copyright: (c) 2014 by The OpenName project
    :license: MIT, see LICENSE for more details.
"""

import os, sys, json, argparse, traceback
from usefulutils import recursive_dict, scrub_dict
from collections import defaultdict
from openspecs import User, userschema
from jsonschema import validate

def recursive_dict_to_dict(rdict):
    d = {}
    for (k,v) in rdict.items():
        if isinstance(v, defaultdict):
            d[k] = recursive_dict_to_dict(v)
        else:
            d[k] = v
    return d

def get_props(schema, parent_prop_names=[]):
    props = []
    for prop_name, prop_value in schema.get('properties', {}).items():
        prop_type = prop_value.get('type', '')
        if prop_type == 'object':
            prop_names = parent_prop_names + [prop_name]
            props.extend(
                get_props(prop_value, prop_names)
            )
        elif prop_type == 'array':
            prop_names = parent_prop_names + [prop_name]
            props.extend(
                get_props(prop_value.get('items', {}), prop_names)
            )
        elif prop_type == 'string':
            prop_names = parent_prop_names + [prop_name]
            props.append(
                ('.'.join(prop_names), prop_type)
            )
    return props

def format_profile_v02(name=None, location=None, bio=None, website=None,
                       avatar_url=None, cover_url=None,
                       twitter_username=None, github_username=None,
                       bitcoin_address=None,
                       pgp_fingerprint=None, pgp_url=None):
    profile = recursive_dict()

    profile['v'] = '0.2'
    
    profile['name']['formatted'] = name
    profile['location']['formatted'] = location
    profile['bio'] = bio
    profile['websites'] = website
    profile['avatar'] = { "url": avatar_url }
    profile['cover'] = { "url": cover_url }
    profile['bitcoin'] = { "address": bitcoin_address }
    profile['twitter'] = { "username": twitter_username }
    profile['github'] = { "username": github_username }
    profile['pgp']['fingerprint'] = pgp_fingerprint
    profile['pgp']['url'] = pgp_url

    return scrub_dict(recursive_dict_to_dict(profile))

def format_profile_v03(name=None, location=None, bio=None, website=None,
                       avatar_url=None, cover_url=None,
                       twitter_username=None, github_username=None,
                       bitcoin_address=None,
                       pgp_fingerprint=None, pgp_url=None):
    
    profile = recursive_dict()

    profile['v'] = '0.3'
    profile['basics']['name'] = name
    profile['basics']['location'] = location
    profile['basics']['bio'] = bio
    if website:
        profile['websites'] = [{ 'url': website }]
    profile['photos'] = []
    if avatar_url:
        profile['photos'].append({ "type": "avatar", "url": avatar_url })
    if cover_url:
        profile['photos'].append({ "type": "cover", "url": cover_url })
    if bitcoin_address:
        profile['payments'] = [{ "type": "bitcoin", "address": bitcoin_address }]
    profile['profiles'] = []
    if twitter_username:
        profile['profiles'].append({ "type": "twitter", "username": twitter_username })
    if github_username:
        profile['profiles'].append({ "type": "github", "username": github_username })
    profile['pgp']['fingerprint'] = pgp_fingerprint
    profile['pgp']['url'] = pgp_url

    return scrub_dict(recursive_dict_to_dict(profile))

def get_raw_profile_data_from_user_input():
    profile = {}

    input_items = [
        { 'name': 'name', 'prompt': 'Name: ' },
        { 'name': 'location', 'prompt': 'Location: ' },
        { 'name': 'bio', 'prompt': 'Bio: ' },
        { 'name': 'website', 'prompt': 'Website: ' },
        { 'name': 'twitter_username', 'prompt': 'Twitter username: ' },
        { 'name': 'github_username', 'prompt': 'Github username: ' },
        { 'name': 'avatar_url', 'prompt': 'Avatar url: ' },
        { 'name': 'cover_url', 'prompt': 'Cover url: ' },
        { 'name': 'bitcoin_address', 'prompt': 'Bitcoin address: ' },
        { 'name': 'pgp_fingerprint', 'prompt': 'PGP Key Fingerprint: ' },
        { 'name': 'pgp_url', 'prompt': 'URL of hosted PGP Public Key: ' },
    ]
    for input_item in input_items:
        profile[input_item['name']] = raw_input(input_item['prompt'])

    return profile

def build_profile_from_user_input():
    raw_data_input = get_raw_profile_data_from_user_input()
    user_dict = format_profile_v02(**raw_data_input)    
    validate(user_dict, userschema)
    return json.dumps(user_dict, indent=4)

if __name__ == '__main__':
    print '\n' + build_profile_from_user_input() + '\n'

