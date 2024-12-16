from typing import Union
import numpy as np
import gmpy2

class Keccak:
    def __init__(self) -> None:
        self.__state = [[np.uint64(0) for _ in range(5)] for _ in range(5)]

    def __RC_LFSR(self, steps: int) -> int:
        result = np.uint64(0x0000000000000001)
        
        for _ in range(1, steps + 1):
            result <<= 1
            if result & 0x0000000000000100:
                result ^= 0x0000000000000071

        return result & 0x0000000000000001

    def __RC(self, round: int) -> int:
        result = np.uint64(0x0000000000000000)
        shift = np.uint64(1)

        for bit in range(0, 7):
            value = np.uint64(self.__RC_LFSR(7 * round + bit))
            result |= value << (shift - 1)
            shift *= 2
        
        return result
    
    def __pad10star1(self, message: Union[str, bytes], rate: int) -> bytes:
        if isinstance(message, str):
            message = message.encode("utf-8")
        
        message_bits = ''.join(f'{byte:08b}' for byte in message)

        padded_bits = message_bits + '1'
        padding_length = (rate - len(padded_bits) % rate - 1) % rate
        padded_bits += '0' * padding_length
        padded_bits += '1'

        padded_message = int(padded_bits, 2).to_bytes((len(padded_bits) + 7) // 8, 'big')
    
        return padded_message


if __name__ == "__main__":
    for _ in range(24):
        test = Keccak()
        round_constant = test._Keccak__RC(_)
        print(f"Round {_}: 0x{round_constant:016x}")
