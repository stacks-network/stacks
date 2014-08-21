# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

# v0.3
schema = {
    "name": "User",
    "title": "ONS User Profile",
    "type": "object",
    "properties": {
        "basics": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string"
                },
                "bio": {
                    "type": "string"
                }
            }
        },
        "names": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "attribute": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "name": {
                        "type": "string"
                    }
                }
            }
        }
        "urls": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "attribute": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "username": {
                        "type": "string"
                    }
                }
            }
        }
        "profiles": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "attribute": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "url": {
                        "type": "string"
                    }
                }
            }
        }
        "images": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "attribute": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "url": {
                        "type": "string"
                    }
                }
            }
        }
        "mail": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "attribute": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "address": {
                        "type": "string"
                    }
                }
            }
        }
        "im": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "attribute": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "address": {
                        "type": "string"
                    }
                }
            }
        }
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
        "v": {
            "type": "string",
            "description": "version number"
        }
    }
}
