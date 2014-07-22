# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

userschema = {
	"name": "User",
	"title": "ONS User Profile",
	"type": "object",
	"properties": {
		"name": {
			"type": "object",
			"properties": {
				"formatted": {
					"type": "string",
				},
			},
		},
		"avatar": {
			"type": "object",
			"properties": {
				"url": {
					"type": "string",
				},
			}
		},
		"cover": {
			"type": "object",
			"properties": {
				"url": {
					"type": "string",
				},
			}
		},
		"location": {
			"type": "object",
			"properties": {
				"formatted": {
					"type": "string",
				},
			},
		},
		"website": {
			"type": "string",
			"description": "the user's website",
		},
		"bio": {
			"type": "string",
			"description": "a short bio about the user",
		},
		"bitcoin": {
			"type": "object",
			"properties": {
				"address": {
					"type": "string",
				},
			},
		},
		"twitter": {
			"type": "object",
			"properties": {
				"username": {
					"type": "string",
				},
				"proof": {
					"type": "object",
					"properties": {
						"url": {
							"type": "string",
						},
					},
				},
			},
		},
		"facebook": {
			"type": "object",
			"properties": {
				"username": {
					"type": "string",
				},
				"proof": {
					"type": "object",
					"properties": {
						"url": {
							"type": "string",
						},
					},
				},
			},
		},
		"github": {
			"type": "object",
			"properties": {
				"username": {
					"type": "string",
				},
				"proof": {
					"type": "object",
					"properties": {
						"url": {
							"type": "string",
						},
					},
				},
			},
		},
		"linkedin": {
			"type": "object",
			"properties": {
				"url": {
					"type": "string",
				},
			},
		},
		"pgp": {
			"type": "object",
			"properties": {
				"url": {
					"type": "string",
				},
				"fingerprint": {
					"type": "string",
				},
			},
		},
		"email": {
			"type": "string",
			"description": "email address",
		},
		"v": {
			"type": "string",
			"description": "version number",
		},
	},
}

import warlock
from usefulutils import to_dict

User = warlock.model_factory(userschema)
User.to_dict = to_dict
