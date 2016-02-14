## Identity Schema RFC (v1)

The ONS Identity Schema is a standard for storing identity information in a flexible and comprehensive way, suitable for public key-value storage networks such as Namecoin.

The standard is versioned to allow for forward and backward compatibility while adding additional features.

Each version of the standard uses a three part semantic version number in the form: (major,minor,patch).

Every version of the standard can be validated against higher level. For example, both a version 1.2 and a version 1.5 schema will be valid version 1 schema. A version 2.3.6 schema and a version 2.3.42 schema will both validate as version 2.3 schemas and also as version 2 schemas.

This allows new features to be added to the standard with a minimum amount of disruption to existing clients.

## Version 1

[View the full version 1 JSON schema](../openspecs/userschema_1/schema-1.json).

The fundemental unit of identity information in version one is an *object*. Related objects are grouped into named *sections*. Each object has exactly one *type*, zero or more *tags*, and a *value*.

Section names, types, tags, and values are all represented as strings.

Section names are defined at the minor version level of this specification, as well as the list of defined types for objects in named sections.

Lists of object tags are defined at the patch level of this specification.

## Structure

The fundemental unit of identity information in version one is an *object*. Related objects are grouped into named *sections*. Each object has exactly one *type*, zero or more *tags*, and a *value*.

Section names, types, tags, and values are all represented as strings.

Section names are defined at the [minor version](004-rfc-identity-schema-v1.0.md) level of this specification.

Lists of object tags  as well as the list of defined types for objects in named sections are defined at the [patch level](005-rfc-identity-schema-v1.0.0.md) of this specification, except for global tags:

### Global tags

* primary
* old

A *primary* tag applied to any object indicates the object should be selected in favor of similar objects which lack this tag.

An *old* tag applied to any object indicates that the object is no longer current and should not be used in the future.

## Rationale

The version 1 schema is designed to be flexible to allow as many types of data to be stored as feasible while maximising backwards and forwards compatibity.

One consequence of this flexibility is that the ability to to strict semantic validation of entries, such as might be performed in a traditional database.

Since ONS data is designed to be stored in decentralized key-value stores, it's not possible for a client to assume any data they query will be properly formatted (phone numbers that look like phone numbers, as opposed to street addresses, for example). Clients must be capable of handing semantically-malformed data regardless of what kind of schema is used.

By using arrays of generic objects, it allows for sections to be inherently one-to-many.

It is frequently the case in identity systems that an identity may posess more than one pice of identity information.

For example, a person might have more than one phone number, or more than one email address, or even more than one name.

Using arrays of objects means that in all cases the proper 1:many relationship can be represented, in order to avoid locking out users whom the designers of less-general specifications may have not considered.

If a user has only one email address, for example, their array will only have a single entry. This means the specification can accodimate them as well as a user with ten email addresses.