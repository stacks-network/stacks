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
		"basics": {
			"type": "object",
			"properties": {
				"name": {
					"type": "string"
				},
				"location": {
					"type": "string"
				},
				"bio": {
					"type": "string"
				}
			}
		},
		"photos": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"type": {
						"type": "string"
					},
					"url": {
						"type": "string"
					}
				}
			}
		},
		"payments": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"type": {
						"type": "string"
					},
					"address": {
						"type": "string"
					},
					"proof": {
						"type": "string"
					}
				}
			}
		},
		"profiles": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"type": {
						"type": "string"
					},
					"username": {
						"type": "string"
					},
					"proof": {
						"type": "string"
					},
					"url": {
						"type": "string"
					}
				}
			}
		},
		"websites": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"label": {
						"type": "string"
					},
					"url": {
						"type": "string"
					}
				}
			}
		},
		"pgp": {
			"type": "object",
			"properties": {
				"url": {
					"type": "string"
				},
				"fingerprint": {
					"type": "string"
				}
			}
		},
		"email": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"label": {
						"type": "string"
					},
					"url": {
						"type": "string"
					}
				}
			}
		},
		"v": {
			"type": "string",
			"description": "version number"
		}
	}
}

import warlock
from usefulutils import to_dict

User = warlock.model_factory(userschema)
User.to_dict = to_dict
