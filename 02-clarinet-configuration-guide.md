Markdown

# Clarinet Configuration Guide: Setup and Troubleshooting

## 1. Configuration Hierarchy
Clarinet enforces a strict separation of concerns between project metadata and execution credentials. Understanding this split is vital for successful deployments.

### 1.1 The Manifest: `Clarinet.toml`
* **Purpose:** Defines contract logic, dependencies, and Clarity versions.
* **Security:** **Public**. Contains NO secrets. Safe for Git.
* **Content:** Links to `.clar` files and external requirements.

### 1.2 The Credentials: `settings/*.toml`
* **Purpose:** Bridges code to the blockchain network (Devnet, Testnet, Mainnet).
* **Security:** **Private**. Contains mnemonics and funds. strictly `.gitignore` this folder in public repos.



## 2. Valid Configuration Patterns
As of Clarinet v2.15.0, strict validation rules apply to the `[accounts.deployer]` block.

### ✅ Supported: 24-Word Mnemonic
This is the standard for production deployments and local Devnet.

```toml
[network]
name = "mainnet"
deployment_fee_rate = 25

[accounts.deployer]
# 24-word mnemonic is MANDATORY
mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art"
derivation = "m/44'/5757'/0'/0/0"
✅ Supported: Encrypted Mnemonic (v3.11+)
Best for shared development environments.

Ini, TOML

[accounts.deployer]
# Ciphertext replaces plaintext mnemonic
encrypted_mnemonic = "U2FsdGVkX19..."
derivation = "m/44'/5757'/0'/0/0"
❌ Deprecated: Raw Private Key
Legacy configurations using secret_key are ignored or cause validation failures in modern Clarinet versions.

Ini, TOML

# DO NOT USE
[accounts.deployer]
secret_key = "753b7c..." 
❌ Rejected: 12-Word Mnemonic
Attempting to use a legacy 12-word phrase will result in a runtime error.

Ini, TOML

# WILL FAIL
mnemonic = "short phrase that is only twelve words long testing failure"
3. Troubleshooting Deployment Failures
Error: bip39 error
Cause: The provided mnemonic does not meet the 24-word length requirement or has an invalid checksum.

Context: Occurs during clarinet deployments generate.

Fix: You must migrate to a 24-word wallet (see Migration Guide).

Error: Insufficient Balance (on a funded wallet)
Cause: Derivation path mismatch.

Scenario: You generated a seed in a generic wallet app, sent STX to it, but Clarinet is looking at a different address derived from that same seed.

Fix: update the derivation field in settings/Mainnet.toml to match your wallet's specific path (e.g., checking account index 1 instead of 0).

4. The "Secret Key" Legacy
You may see older tutorials referencing secret_key. This field was deprecated because a single private key cannot support Deterministic Actor Generation. Clarinet's testing suite requires the ability to generate wallet_1, wallet_2, etc., from a single root to simulate complex contract interactions. A raw private key lacks this hierarchical capability.


---
