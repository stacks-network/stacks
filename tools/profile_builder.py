# -*- coding: utf-8 -*-
"""
    OpenName
    ~~~~~

    :copyright: (c) 2014 by The OpenName project
    :license: MIT, see LICENSE for more details.
"""

import os, sys, json, argparse, traceback
from usefulutils import recursive_dict, scrub_dict, recursive_dict_to_dict
from collections import defaultdict
from openspecs import userschema, userschema_rfc
from jsonschema import validate


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
    profile['website'] = website
    profile['avatar'] = {"url": avatar_url}
    profile['cover'] = {"url": cover_url}
    profile['bitcoin'] = {"address": bitcoin_address}
    profile['twitter'] = {"username": twitter_username}
    profile['github'] = {"username": github_username}
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
        profile['websites'] = [{'url': website}]
    profile['photos'] = []
    if avatar_url:
        profile['photos'].append({"type": "avatar", "url": avatar_url})
    if cover_url:
        profile['photos'].append({"type": "cover", "url": cover_url})
    if bitcoin_address:
        profile['payments'] = [{"type": "bitcoin", "address": bitcoin_address}]
    profile['profiles'] = []
    if twitter_username:
        profile['profiles'].append({"type": "twitter", "username": twitter_username})
    if github_username:
        profile['profiles'].append({"type": "github", "username": github_username})
    profile['pgp']['fingerprint'] = pgp_fingerprint
    profile['pgp']['url'] = pgp_url

    return scrub_dict(recursive_dict_to_dict(profile))


def get_raw_profile_data_from_user_input():
    profile = {}

    input_items = [
        {'name': 'name', 'prompt': 'Name: '},
        {'name': 'location', 'prompt': 'Location: '},
        {'name': 'bio', 'prompt': 'Bio: '},
        {'name': 'website', 'prompt': 'Website: '},
        {'name': 'twitter_username', 'prompt': 'Twitter username: '},
        {'name': 'github_username', 'prompt': 'Github username: '},
        {'name': 'avatar_url', 'prompt': 'Avatar url: '},
        {'name': 'cover_url', 'prompt': 'Cover url: '},
        {'name': 'bitcoin_address', 'prompt': 'Bitcoin address: '},
        {'name': 'pgp_fingerprint', 'prompt': 'PGP Key Fingerprint: '},
        {'name': 'pgp_url', 'prompt': 'URL of hosted PGP Public Key: '},
    ]
    for input_item in input_items:
        profile[input_item['name']] = raw_input(input_item['prompt'])

    return profile


def build_profile_from_user_input():
    parser = argparse.ArgumentParser(description='Build an open name system user profile from user input.')
    parser.add_argument('-version', metavar='v', choices=['0.2', '0.3'],
                        default='0.2', help='the schema version')
    args = parser.parse_args()

    raw_data_input = get_raw_profile_data_from_user_input()

    if args.version == '0.2':
        user_dict = format_profile_v02(**raw_data_input)
        validate(user_dict, userschema.schema)
    elif args.version == '0.3':
        user_dict = format_profile_v03(**raw_data_input)
        validate(user_dict, userschema_rfc.schema)

    return json.dumps(user_dict, indent=4)

if __name__ == '__main__':
    print '\n' + build_profile_from_user_input() + '\n'
