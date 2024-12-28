from typing import Union
from .keccak import Keccak

class SHA3:
    def __init__(self, output_length: int = 256) -> None:
        if output_length not in [224, 256, 384, 512]:
            raise ValueError("Output length must be one of: 224, 256, 384, 512")
            
        self.output_length = output_length
        self.keccak = Keccak()
        
    def hash(self, message: Union[str, bytes]) -> str:
        return self.keccak.hash(message, self.output_length)
        
    @classmethod
    def sha3_224(cls, message: Union[str, bytes]) -> str:
        return cls(224).hash(message)
        
    @classmethod
    def sha3_256(cls, message: Union[str, bytes]) -> str:
        return cls(256).hash(message)
        
    @classmethod
    def sha3_384(cls, message: Union[str, bytes]) -> str:
        return cls(384).hash(message)
        
    @classmethod
    def sha3_512(cls, message: Union[str, bytes]) -> str:
        return cls(512).hash(message)