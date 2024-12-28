from typing import Union, List

class Keccak:
    def __init__(self) -> None:
        self.state = self.__state_init()

    def __rotate_left(self, x, n):
        return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

    def __state_init(self):
        return [[0 for _ in range(5)] for _ in range(5)]

    def __RC_LFSR(self, steps: int) -> int:
        result = 0x0000000000000001
        for _ in range(steps):
            msb = result >> 7
            result = (result << 1) & 0xFF
            if msb:
                result ^= 0x71
        return result & 0x1

    def __RC(self, round: int) -> int:
        result = 0
        for j in range(7):
            if self.__RC_LFSR(j + 7 * round):
                result ^= 1 << ((1 << j) - 1)
        return result

    def __pad10star1(self, message: Union[str, bytes], rate: int) -> bytes:
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        rate_bytes = rate // 8
        padding_length = rate_bytes - (len(message) % rate_bytes)
        
        suffix = 0x06
        
        if padding_length == 1:
            padded = message + bytes([suffix | 0x80])
        else:
            padded = message + bytes([suffix]) + bytes([0] * (padding_length - 2)) + bytes([0x80])
        
        return padded

    def __absorb_block(self, state, block):
        for i in range(0, len(block), 8):
            lane = int.from_bytes(block[i:i+8].ljust(8, b'\x00'), 'little')
            x = (i // 8) % 5
            y = (i // 8) // 5
            state[x][y] ^= lane
        return state

    def __theta(self, state):
        C = [0] * 5
        D = [0] * 5
        
        for x in range(5):
            C[x] = state[x][0] ^ state[x][1] ^ state[x][2] ^ state[x][3] ^ state[x][4]
        
        for x in range(5):
            D[x] = C[(x-1)%5] ^ self.__rotate_left(C[(x+1)%5], 1)
        
        for x in range(5):
            for y in range(5):
                state[x][y] ^= D[x]
        
        return state

    def __rho(self, state):
        rho_offsets = [
            [0, 36, 3, 41, 18],
            [1, 44, 10, 45, 2],
            [62, 6, 43, 15, 61],
            [28, 55, 25, 21, 56],
            [27, 20, 39, 8, 14]
        ]
        
        for x in range(5):
            for y in range(5):
                state[x][y] = self.__rotate_left(state[x][y], rho_offsets[x][y])
        
        return state

    def __pi(self, state):
        new_state = self.__state_init()
        for x in range(5):
            for y in range(5):
                new_x = y
                new_y = (2*x + 3*y) % 5
                new_state[new_x][new_y] = state[x][y]
        return new_state

    def __chi(self, state):
        new_state = self.__state_init()
        for x in range(5):
            for y in range(5):
                new_state[x][y] = state[x][y] ^ ((~state[(x+1)%5][y]) & state[(x+2)%5][y])
        return new_state

    def __iota(self, state, round_index):
        state[0][0] ^= self.__RC(round_index)
        return state

    def __round(self, state, round_index):
        state = self.__theta(state)
        state = self.__rho(state)
        state = self.__pi(state)
        state = self.__chi(state)
        state = self.__iota(state, round_index)
        return state

    def __keccak_f(self, state):
        for round_index in range(24):
            state = self.__round(state, round_index)
        return state

    def hash(self, message: Union[str, bytes], output_length: int = 256) -> str:
        if output_length not in [224, 256, 384, 512]:
            raise ValueError("Output length must be one of: 224, 256, 384, 512")
        
        rate = 1600 - (output_length * 2)  # capacity = output_length * 2
        state = self.__state_init()
        
        padded_message = self.__pad10star1(message, rate)
        
        for i in range(0, len(padded_message), rate // 8):
            block = padded_message[i:i + rate // 8]
            state = self.__absorb_block(state, block)
            state = self.__keccak_f(state)
        
        output = bytearray()
        output_bytes = output_length // 8
        
        while len(output) < output_bytes:
            output_block = bytearray()
            for y in range(5):
                for x in range(5):
                    if len(output_block) < rate // 8:
                        lane_bytes = state[x][y].to_bytes(8, 'little')
                        output_block.extend(lane_bytes)
            
            output.extend(output_block[:output_bytes - len(output)])
            
            if len(output) < output_bytes:
                state = self.__keccak_f(state)
        
        return output.hex()