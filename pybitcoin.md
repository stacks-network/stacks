---
title: Pybitcoin
description: A Python library for working with private and public keys, addresses, transactions, and RPC calls
image: https://images.unsplash.com/photo-1430760903787-4d91bbf15384?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&w=1080&fit=max&s=98326a6e44d1b6bbcddb0d89f75ed95c
next: faq
---

### Installation

```bash
$ pip install pybitcoin
```

### Private Keys

```python
>>> from pybitcoin import BitcoinPrivateKey
>>> private_key = BitcoinPrivateKey()
>>> private_key.to_hex()
'91149ee24f1ee9a6f42c3dd64c2287781c8c57a6e8e929c80976e586d5322a3d'
>>> private_key.to_wif()
'5JvBUBPzU42Y7BHD7thTnySXQXMk8XEJGGQGcyBw7CCkw8RAH7m'
>>> private_key_2 = BitcoinPrivateKey('91149ee24f1ee9a6f42c3dd64c2287781c8c57a6e8e929c80976e586d5322a3d')
>>> print private_key.to_wif() == private_key_2.to_wif()
True
```

### Public Keys

```python
>>> public_key = private_key.public_key()
>>> public_key.to_hex()
'042c6b7e6da7633c8f226891cc7fa8e5ec84f8eacc792a46786efc869a408d29539a5e6f8de3f71c0014e8ea71691c7b41f45c083a074fef7ab5c321753ba2b3fe'
>>> public_key_2 = BitcoinPublicKey(public_key.to_hex())
>>> print public_key.to_hex() == public_key_2.to_hex()
True
```

### Addresses

```python
>>> public_key.address()
'13mtgVARiB1HiRyCHnKTi6rEwyje5TYKBW'
>>> public_key.hash160()
'1e6db1e09b5e307847e5734864a79ea0113d0083'
```

### Sending Basic Transactions

```python
>>> from pybitcoin import BlockcypherClient
>>> recipient_address = '1EEwLZVZMc2EhMf3LXDARbp4mA3qAwhBxu'
>>> blockchain_client = BlockcypherClient(BLOCKCYPHER_API_KEY)
>>> send_to_address(recipient_address, 10000, private_key.to_hex(), blockchain_client)
```

### Sending OP_RETURN Transactions

```python
>>> from pybitcoin import make_op_return_tx
>>> data = '00' * 80
>>> tx = make_op_return_tx(data, private_key.to_hex(), blockchain_client, fee=10000, format='bin')
>>> broadcast_transaction(tx, blockchain_client)
{"success": True}
```

