---
title: Blockstack Profiles - Python
description: A Python library for creating, signing, and verifying Blockstack profiles
image: /images/article-photos/computer-2.jpg
next: pybitcoin
---

#### Installation

```bash
$ pip install blockstack-profiles
```

#### Package Importing

```python
from blockstack_profiles import (
    sign_token_record, sign_token_records, verify_token_record,
    get_profile_from_tokens, make_zone_file_for_hosted_data
)
```

#### Defining Keys

```python
private_key = "89088e4779c49c8c3210caae38df06193359417036d87d3cc8888dcfe579905701"
public_key = "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
```

#### Creating Profiles

```python
profile = { "name": "Naval Ravikant", "birthDate": "1980-01-01" }
profile_components = [
    {"name": "Naval Ravikant"},
    {"birthDate": "1980-01-01"}
]
```

#### Signing Token Records

```python
token_records = sign_token_records(profile_components, private_key)
```

##### Example output:

```json
[
  {
    "decoded_token": {
      "issuedAt": "2016-03-02T18:59:29.043308", 
      "claim": {
        "name": "Naval Ravikant"
      }, 
      "expiresAt": "2017-03-02T18:59:29.043308", 
      "subject": {
        "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
      }
    }, 
    "token": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3N1ZWRBdCI6IjIwMTYtMDMtMDJUMTg6NTk6MjkuMDQzMzA4IiwiY2xhaW0iOnsibmFtZSI6Ik5hdmFsIFJhdmlrYW50In0sImV4cGlyZXNBdCI6IjIwMTctMDMtMDJUMTg6NTk6MjkuMDQzMzA4Iiwic3ViamVjdCI6eyJwdWJsaWNLZXkiOiIwM2U5OTUzY2IxODRiMGMyNTNlMWM1YTk2ZGY0Y2I5OTMzYmY4OWVkMmRmNWJkNzliMDJmNzFjY2ZlNWVjNTAyNjgifX0.0qQbEXTsDSbswL2qfMVzMuYU503ddfclXz3ict1rh85arXX47DW51814n1OFOAzjGoeDvsQXpfG3hB2dMHuIEw", 
    "parentPublicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e", 
    "encrypted": false, 
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  }, 
  {
    "decoded_token": {
      "issuedAt": "2016-03-02T18:59:29.043308", 
      "claim": {
        "birthDate": "1980-01-01"
      }, 
      "expiresAt": "2017-03-02T18:59:29.043308", 
      "subject": {
        "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
      }
    }, 
    "token": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3N1ZWRBdCI6IjIwMTYtMDMtMDJUMTg6NTk6MjkuMDQzMzA4IiwiY2xhaW0iOnsiYmlydGhEYXRlIjoiMTk4MC0wMS0wMSJ9LCJleHBpcmVzQXQiOiIyMDE3LTAzLTAyVDE4OjU5OjI5LjA0MzMwOCIsInN1YmplY3QiOnsicHVibGljS2V5IjoiMDNlOTk1M2NiMTg0YjBjMjUzZTFjNWE5NmRmNGNiOTkzM2JmODllZDJkZjViZDc5YjAyZjcxY2NmZTVlYzUwMjY4In19.m-v3mrPtXaNSltBvWfOLnpPerIxJhQQOt0-x-Lyw1A-iGp_dq8TPLrYGqo4UfcBfqva52-N5eSCN6c1pKgSLDQ", 
    "parentPublicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e", 
    "encrypted": false, 
    "publicKey": "02f1fd79dcd51bd017f71546ddc0fd3c8fb7de673da8661c4ceec0463dc991cc7e"
  }
]
```

#### Verifying Token Records

```python
try:
    decoded_token = verify_token_record(token_records[0], public_key)
except:
    print "Invalid token"
```

#### Recovering Profiles

```python
profile = get_profile_from_tokens(token_records, public_key)
```

#### Creating Zone Files

```python
username = "naval.id"
hosted_data_url = "https://blockstack.s3.amazonaws.com/naval.id.json"
zone_file = make_zone_file_for_hosted_data(username, hosted_data_url)
```

```
$ORIGIN naval.id
$TTL 3600
@ IN URI "https://blockstack.s3.amazonaws.com/naval.id/naval.id.json"
```
