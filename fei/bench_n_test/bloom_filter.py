from bitarray import bitarray
from hashlib import sha1

def func():
    a = bitarray()
    # a.append(True)
    # a.extend([True, True, False, False, True])
    a.append(0)
    a.append(1)
    print(a)

def func2():
    print(sha1(b'a', b'kk'))

class BloomFilter():
    def __init__(self, size, hash_count):
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

        self.size = size
        self.hash_count = hash_count

    def __len__(self):
        return self.size

    def add(self, item):
        for i in range(self.hash_count):
            sign = sha1((str(item) + str(i)).encode('utf-8')).hexdigest()
            index = int(sign, 16) % self.size
            self.bit_array[index] = 1

        # print(self.bit_array)

    def __contains__(self, item):
        find_or_not = True
        for i in range(self.hash_count):
            sign = sha1((str(item) + str(i)).encode('utf-8')).hexdigest()
            index = int(sign, 16) % self.size
            if self.bit_array[index] == 0:
                find_or_not = False
        return find_or_not

        
if __name__ == '__main__':
    size, hash_count = 20000000, 5
    bf = BloomFilter(size, hash_count)
    bf.add('abc')
    bf.add('kkk')
    print('abc' in bf)
    print('kkk' in bf)
    print('xxx' in bf)

    bf.add(1)
    bf.add(2)
    bf.add(3)
    print(1 in bf)
    print(2 in bf)
    print(3 in bf)
    # print(bf.bit_array)
    for i in range(10000):
        bf.add(i)
    
    for i in range(10000, 20000):
        if (i in bf):
            print(i)