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
        "fingerprints": {
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
                    "fingerprint": {
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
        "locations": {
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
                    "location": {
                        "type": "string"
                    }
                }
            }
        }
        "text": {
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
                    "text": {
                        "type": "string"
                    }
                }
            }
        }
        "proof": {
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
                    "location": {
                        "type": "string"
                    }
                }
            }
        }
        "v": {
            "type": "string",
            "description": "version number"
        }
    }
}
