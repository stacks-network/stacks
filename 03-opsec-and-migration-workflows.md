
# Operational Security & Migration Workflows

## 1. Migration Strategy: 12-Word to 24-Word
Clarinet does not offer a "compatibility mode" for legacy 12-word wallets. If your deployment funds are in a 12-word wallet, you must perform a key rotation.

### The Migration Workflow
1.  **Generate Identity:** Use a secure, offline-capable tool (like `bip39-cli` or a hardware wallet) to generate a new 24-word mnemonic.
2.  **Derive Address:** Identify the public Stacks (SP...) address associated with this new seed.
3.  **Fund Transfer:** Execute an on-chain transfer of STX from the old 12-word wallet to the new 24-word wallet.
4.  **Reconfigure:** Update `settings/Mainnet.toml` with the new mnemonic.

> **Warning:** This effectively forces a rotation of keys. Ensure you update any hardcoded references to the deployer address in your dApps or off-chain indexers.

## 2. CI/CD Pipeline Security
Automated deployments (GitHub Actions, GitLab CI) present specific challenges because there is no human to enter a password for encrypted mnemonics.



### Best Practices for CI/CD
1.  **Environment Variables:** Store the 24-word mnemonic as a **Secret** in your CI platform (e.g., `STACKS_DEPLOYER_MNEMONIC`).
2.  **Dynamic Injection:** Use a build script to inject the secret into `settings/Mainnet.toml` at runtime.
3.  **Quoting:** You must handle the spaces in the mnemonic carefully.

**Example Injection Pattern:**
```bash
# Ensure the mnemonic is quoted to treat spaces as a single string
sed -i "s|DEPLOYER_MNEMONIC_PLACEHOLDER|$STACKS_DEPLOYER_MNEMONIC|g" settings/Mainnet.toml
```

3. Local Development Security: Encryption
For local development, especially on machines that might be shared or physically accessible, never store plaintext mnemonics.

Using Clarinet Encryption (v3.11+):

Run the encryption command:

```bash

clarinet deployments encrypt
```
Enter your 24-word phrase and a strong password.

Clarinet will return a ciphertext (e.g., U2FsdGVkX1...).

Replace mnemonic with encrypted_mnemonic in your config.

Runtime Behavior: When you run clarinet deployments apply, the CLI will detect the encrypted field and pause execution to request the password via stdin. This adds a layer of Multi-Factor Authentication (Something you have + Something you know).

4. Hardware Wallet Integration
For high-value contract deployments, the gold standard is offline signing.

While Clarinet requires a mnemonic for automation, you can decouple the Build and Sign steps:

Use Clarinet to generate the raw transaction payload.

Transfer the payload to an air-gapped machine or use stacks.js to sign it with a hardware wallet (Ledger/Trezor).

Broadcast the signed transaction separately.

This method avoids ever exposing the mnemonic to the development machine's file system, essentially bypassing the settings.toml risk entirely.
