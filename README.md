# SHA3 Implementation in Pure Python

A pure Python implementation of the SHA3 (Keccak) hash function family, following the NIST FIPS 202 standard.

## Features

- Pure Python implementation (no external dependencies)
- Supports all standard SHA3 variants:
  - SHA3-224
  - SHA3-256
  - SHA3-384
  - SHA3-512
- Accepts both string and binary input
- Comprehensive test suite with NIST test vectors

## Installation

```bash
pip install .
```

## Usage

```python
from sha3 import sha3_256, sha3_512

hash_value = sha3_256("Hello, World!")
print(hash_value)

hash_224 = sha3_224("Hello, World!")
hash_384 = sha3_384("Hello, World!")
hash_512 = sha3_512("Hello, World!")

binary_data = b"Hello, World!"
hash_value = sha3_256(binary_data)
```

## Development

To set up the development environment:

```bash
pip install -r requirements.txt

pytest tests/
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.