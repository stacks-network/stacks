## Proof Schema RFC (v0.1)

### Format

An ONS proof block is an array of digitally signed attestations one user makes regarding the validity of another user's (or their own) identity information.

Each proof object contains an assestation regarding one piece of identity information.

### Sections of a Proof

#### Rater

The name of the identity who has signed the proof.

This field is mandatory.

#### Ratee

The name of the identity whose information is being certified.

This field is mandatory.

#### Negative

If this field is set to <code>true</code>, the rater is claiming that the identified object is incorrect.

This field is optional.

#### Date

A date or date and time in ISO 8601 format which specifies the point in time at which the proof was generated.

This field is optional.

#### Start

A date or date and time in ISO 8601 format which specifies the earliest point in time at which the proof should be considered valid.

This field is optional.

#### End

A date or date and time in ISO 8601 format which specifies the latest point in time at which the proof should be considered valid.

This field is optional.

#### Object

A 20 byte string formed by taking the Bitcoin Hash160 of an object in an ONS entry.

The object should be formatted as a JSON object with a label corresponding to the name of the array it is found in in canonical form.

##### Example

<pre><code>{ images: { "type": "avatar", "url": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg" } }</code></pre>

This field is mandatory.

#### Type

The type of public key used to generate the signature. The public key should be listed in the ratee's ONS entry as <code>fingerprint</code> object or be an address listed as a <code>payments</code> object.

This field is mandatory.

##### Examples

If the type of proof is "pgp", then the proof should be signed by a public key whose fingerprint is listed as a <code>type: "pgp"</code> Fingerprints object.

If the type of proof is "litecoin", then the proof should be signed by an address listed as a <code>type: "litecoin"</code> Payments object.

#### Signature

The signature of the proof.

To generate the signature, the proof object should be constructed with a blank signature field and verified similarly.

This field is mandatory.

### Self-Verifying Proofs

In the case where a user is verifying their ownership of a public key listed in their ONS profile, the rater and ratee fields should both be set to the user's name.

### Dates and Proofs

The proof object has three optional fields which can be used to give the proof greater temporal precision.

Since nearly every piece of data contained in an ONS entry is subject to change, it can be beneficial for a rater to specify a time component to their attestation. For example, certifying that a user lives at a given location today does not necessarily imply anything about where the lived yesterday or will live tomorrow.

If users ever desire to evalulating other users based on the accuracy of their attestations, then giving them the ability to set temporal limits on their claims will be necessary.

#### Rules

A date value by itself implicitly indicates the proof is true for the given date, with no positive or negative claims implied for any past or future dates. If there are two proof that are identical except for the data, the proof with the newest date should be considered current.

A start value by itself indicates the proof transitioned from false to true (or true to false, for negative proofs) at the given date, with no positive or negative claims implied for any point after the start date.

An end value by itself indicates the proof transitioned from true to false (false to true) at the given date, with no positive or negative claims implied for any point before the end date.

A start combined with an end value indicates an inclusive range of date in which the proof was true (or false).

### Example

The object being rated is: 

<pre><code>
{ images: { "type": "avatar", "url": "https://pbs.twimg.com/profile_images/3696617328/667874c5936764d93d56ccc76a2bcc13.jpeg" } }
</code></pre>

The finished proof object is:

<pre><code>
{[
    "proof": {
        "rater": "u/me",
        "ratee": "id/you",
        "object": "d9779cb38a5fc5b93a739e086ede1abbce29df8b",
        "type": "bitcoin",
        "signature": "HAOHHIRgr1218Dp6ffAcqdW3A8/5EklYVrvpD3K8kJQmCONOfH7eVwl1dj6HjiJkRaD85nLgC1T2nrWUgtz6D8g="
    }],
    "v": "0.1"
}
</code></pre>

**Note**: to sign and verify the proof, it is placed in a single line canonical form with the signature field empty as shown:

<pre><code>{ "proof": { "rater": "u/me", "ratee": "id/you", "object": "d9779cb38a5fc5b93a739e086ede1abbce29df8b", "type": "bitcoin", "signature": "" } }</code></pre>
