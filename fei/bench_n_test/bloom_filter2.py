from bitarray import bitarray
from hashlib import sha1

class BloomFilter():
    def __init__(self, bit_length, hash_count):
        self.bit_array = bitarray(bit_length)
        self.bit_array.setall(0)

        self.bit_length = bit_length
        self.hash_count = hash_count

    def add(self, item):
        for i in range(self.hash_count):
            index = self._get_index(item, i)
            # print(f'debug: index = {index}, current hash_count = {i}')
            self.bit_array[index] = 1

    def if_exist(self, item):
        for i in range(self.hash_count):
            index = self._get_index(item, i)
            if self.bit_array[index] == 0:
                return False
        return True

    def _get_index(self, item, current_hash_count):
        sign = sha1((str(item) + str(current_hash_count)).encode('utf-8')).hexdigest()
        index = int(sign, 16) % self.bit_length
        return index

if __name__ == '__main__':
    BIT_LENGTH, HASH_COUNT = 3000000, 5
    test_data_count = 300000

    import time
    START = int(time.time())
    bloom_filter = BloomFilter(BIT_LENGTH, HASH_COUNT)
    # DURATION 1
    T1 = int(time.time())
    for i in range(test_data_count):
        bloom_filter.add(i)

    # DURATION 2
    T2 = int(time.time())
    # test
    count = 0
    for i in range(test_data_count + 20000, test_data_count + 30000):
        if bloom_filter.if_exist(i):
            count += 1
            print(f"current: {count}, and got one: {i}")
    # DURATION 3
    T3 = int(time.time())
    
    count_bit_1 = 0
    for bit in bloom_filter.bit_array:
        if bit == 1:
            count_bit_1 += 1
    print(f'COUNT BIT 1: {count_bit_1}')
    # DURATION 4
    T4 = int(time.time())
    
    print(f'DURATION 1 - init: {START - T1}')
    print(f'DURATION 2 - add: {T2 - T1}')
    print(f'DURATION 3 - check: {T3 - T2}')
    print(f'DURATION 4 - count bit: {T4 - T3}')