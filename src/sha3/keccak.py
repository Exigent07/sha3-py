from typing import Union, List
import numpy as np
import gmpy2

class Keccak:
    def __init__(self) -> None:
        None
        
    def __rotate_left(self, x, n):
        return ((x << n) | (x >> (64 - n))) & np.uint64(0xFFFFFFFFFFFFFFFF)

    def __state_init(self):
        return [[np.uint64(0) for _ in range(5)] for _ in range(5)]

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
    
    def __pad10star1(self, message: Union[str, bytes], rate: int) -> List[bytes]:
        if isinstance(message, str):
            message = message.encode("utf-8")
        
        message_bits = ''.join(f'{byte:08b}' for byte in message)

        padded_bits = message_bits + '1'
        padding_length = (rate - len(padded_bits) % rate - 1) % rate
        padded_bits += '0' * padding_length
        padded_bits += '1'

        padded_message = int(padded_bits, 2).to_bytes((len(padded_bits) + 7) // 8, 'big')
    
        return padded_message
    
    def __absorb_block(self, state, block):
        for i in range(0, 25):
            state[i // 5][i % 5] ^= block[i]

        return state
    
    def __theta(self, state):
        C = [np.uint64(0) for _ in range(5)]
        D = [np.uint64(0) for _ in range(5)]
        
        for x in range(5):
            C[x] = state[x][0] ^ state[x][1] ^ state[x][2] ^ state[x][3] ^ state[x][4]

        for x in range(5):
            D[x] = C[(x - 1) % 5] ^ self.__rotate_left(C[(x + 1) % 5], 1)

        for x in range(5):
            for y in range(5):
                state[x][y] ^= D[x]

        return state


if __name__ == "__main__":
    for _ in range(24):
        test = Keccak()
        round_constant = test._Keccak__RC(_)
        print(f"Round {_}: 0x{round_constant:016x}")
