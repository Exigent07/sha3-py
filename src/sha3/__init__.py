from .hash import SHA3

__version__ = "0.1.0"

sha3_224 = SHA3.sha3_224
sha3_256 = SHA3.sha3_256
sha3_384 = SHA3.sha3_384
sha3_512 = SHA3.sha3_512

__all__ = [
    "SHA3",
    "sha3_224",
    "sha3_256",
    "sha3_384",
    "sha3_512",
]