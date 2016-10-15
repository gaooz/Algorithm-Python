# encoding=utf-8
# gaooz.com
# 2016-10-15

class simhash:

    def __init__(self, tokens='', hashbits=128):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens);

    def __str__(self):
        return str(self.hash)

    #生成simhash值
    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_hash(x) for x in tokens]: #t为token的普通hash值
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask :
                    v[i] += 1
                else:
                    v[i] -= 1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint

    #求海明距离
    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0;
        while x :
            tot += 1
            x &= x - 1
        return tot

    #求相似度
    def similarity (self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b : return b / a
        else: return a / b

    #针对source生成hash值   (一个可变长度版本的Python的内置散列)
    def _string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x

if __name__ == '__main__':
    s = 'Hi Qi Niu'
    hash1 = simhash(s.split())

    s = 'Qi Niu Crop is a very NiuBi cloud storage'
    hash2 = simhash(s.split())

    s = 'I want to go to Qi Niu'
    hash3 = simhash(s.split())

    print(hash1.hamming_distance(hash2) , hash1.similarity(hash2))
    print(hash1.hamming_distance(hash3) ,  hash1.similarity(hash3))