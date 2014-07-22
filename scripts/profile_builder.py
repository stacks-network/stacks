# -*- coding: utf-8 -*-
"""
    OpenName
    ~~~~~

    :copyright: (c) 2014 by The OpenName project
    :license: MIT, see LICENSE for more details.
"""

import os, sys, json, argparse, traceback
from jsonschema import validate
from usefulutils import recursive_dict
from onsuserschema import User, user_schema

def format_profile_v03(name=None, location=None, bio=None, website=None,
					   avatar_url=None, cover_url=None,
					   twitter_username=None, github_username=None,
					   bitcoin_address=None,
					   pgp_fingerprint=None, pgp_url=None):
	
	profile = recursive_dict()

	profile = {
		'basics': {},
		'photos': [],
		'payments': [],
		'profiles': [],
		'pgp': {},
		'email': [],
		'v': '0.3',
	}
	
	if name:
		profile['basics']['name'] = name
	if location:
		profile['basics']['location'] = location
	if bio:
		profile['basics']['bio'] = bio
	if website:
		profile['websites'] = [{ 'url': website }]

	if avatar_url:
		profile['photos'].append({ "type": "avatar", "url": avatar_url })
	if cover_url:
		profile['photos'].append({ "type": "cover", "url": cover_url })

	if bitcoin_address:
		profile['payments'].append({ "type": "bitcoin", "address": bitcoin_address })

	if twitter_username:
		profile['profiles'].append({ "type": "twitter", "username": twitter_username })
	if github_username:
		profile['profiles'].append({ "type": "github", "username": github_username })

	if pgp_fingerprint:
		profile['pgp']['fingerprint'] = pgp_fingerprint
	if pgp_url:
		profile['pgp']['url'] = pgp_url

	return profile

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

if __name__ == '__main__':
	raw_profile_data = get_raw_profile_data_from_user_input()
	uncleaned_profile_dict = format_profile_v03(**raw_profile_data)
	user = User(**uncleaned_profile_dict)
	user_dict = user.to_dict()
	validate(user_dict, user_schema)
	print json.dumps(user_dict)
