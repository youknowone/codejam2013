
import sys
import time
from qrc import *

stime = time.time()

caches = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002, 10000001, 10011001, 10100101, 10111101, 11000011, 11011011, 11100111, 11111111, 20000002, 100000001, 100010001, 100020001, 100101001, 100111001, 100121001, 101000101, 101010101, 101020101, 101101101, 101111101, 110000011, 110010011, 110020011, 110101011, 110111011, 111000111, 111010111, 111101111, 111111111, 200000002, 200010002, 1000000001, 1000110001, 1001001001, 1001111001, 1010000101, 1010110101, 1011001101, 1011111101, 1100000011, 1100110011, 1101001011, 1101111011, 1110000111, 1110110111, 1111001111, 2000000002, 10000000001, 10000100001, 10000200001, 10001010001, 10001110001, 10001210001, 10010001001, 10010101001, 10010201001, 10011011001, 10011111001, 10100000101, 10100100101, 10100200101, 10101010101, 10101110101, 10110001101, 10110101101, 10111011101, 10111111101, 11000000011, 11000100011, 11000200011, 11001010011, 11001110011, 11010001011, 11010101011, 11011011011, 11011111011, 11100000111, 11100100111, 11101010111, 11101110111, 11110001111, 11110101111, 20000000002, 20000100002, 100000000001, 100001100001, 100010010001, 100011110001, 100100001001, 100101101001, 100110011001, 100111111001, 101000000101, 101001100101, 101010010101, 101011110101, 101100001101, 101101101101, 101110011101, 110000000011, 110001100011, 110010010011, 110011110011, 110100001011, 110101101011, 110110011011, 111000000111, 111001100111, 111010010111, 111100001111, 200000000002, 1000000000001, 1000001000001, 1000002000001, 1000010100001, 1000011100001, 1000012100001, 1000100010001, 1000101010001, 1000102010001, 1000110110001, 1000111110001, 1001000001001, 1001001001001, 1001002001001, 1001010101001, 1001011101001, 1001100011001, 1001101011001, 1001110111001, 1001111111001, 1010000000101, 1010001000101, 1010002000101, 1010010100101, 1010011100101, 1010100010101, 1010101010101, 1010110110101, 1010111110101, 1011000001101, 1011001001101, 1011010101101, 1011011101101, 1011100011101, 1011101011101, 1100000000011, 1100001000011, 1100002000011, 1100010100011, 1100011100011, 1100100010011, 1100101010011, 1100110110011, 1100111110011, 1101000001011, 1101001001011, 1101010101011, 1101011101011, 1101100011011, 1101101011011, 1110000000111, 1110001000111, 1110010100111, 1110011100111, 1110100010111, 1110101010111, 1111000001111, 1111001001111, 2000000000002, 2000001000002]

palindromes = set([])
def is_palindrome(num):
    if num in palindromes:
        return True
    snum = str(num)
    lsnum = len(snum)
    for i in xrange(0, lsnum / 2):
        if snum[i] != snum[lsnum - i - 1]:
            return False
    palindromes.add(num)
    return True

def gen_palindrome1(snum):
    lnum = len(snum)
    if lnum == 1:
        return snum
    return snum + snum[lnum-2::-1]

def gen_palindrome2(snum):
    return snum + snum[::-1]

def gen_palindrome3(snum):
    return snum + '0' + snum[::-1]

def gen_palindrome4(snum):
    return snum + '1' + snum[::-1]

def gen_palindrome5(snum):
    return snum + '2' + snum[::-1]

def get_seed1(snum):
    lnum = len(snum)
    tlen = lnum / 2 + lnum % 2
    return '1' + '0' * (tlen-1)
    return snum[:tlen]

def get_seed2(snum):
    lnum = len(snum)
    tlen = lnum / 2 + lnum % 2
    return '9' * tlen

def combination(length):
    n = 1
    yield '1'
    cur = ['1']
    while n < length:
        new = []
        for x in cur:
            a, b = x + '0', x + '1'
            yield a
            yield b
            new.append(a)
            new.append(b)
        cur = new
        n += 1

def gen_0():
    pals = [1, 2, 3]
    spals = [1, 4, 9]
    return pals, spals

LEN = 25

def gen_1():
    pals = []
    spals = []
    candidates = combination(LEN)
    for i, c in enumerate(candidates):
        for spal in gen_palindrome2(c), gen_palindrome3(c), gen_palindrome4(c), gen_palindrome5(c):
            pal = long(spal)
            spal = pal ** 2
            if is_palindrome(spal):
                pals.append(pal)
                spals.append(spal)
        #if i % 100000 == 0:
        #    sys.stdout.write('%d/%d(%.2f) %d\n' % (i, 33500000, 1.0*i/33500000, int(time.time() - stime)))
        #    sys.stdout.flush()
    return pals, spals

def gen_2():
    pals = []
    spals = []
    for i in xrange(0, LEN):
        zeros = '0' * i
        sn1 = '2' + zeros + zeros + '2'
        sn2 = '2' + zeros + '0' + zeros + '2'
        sn3 = '2' + zeros + '1' + zeros + '2'
        for sn in sn1, sn2, sn3:
            n = long(sn)
            sn = n ** 2
            if is_palindrome(sn):
                pals.append(n)
                spals.append(sn)
    return pals, spals

def gen_all():
    pals, spals = [], []
    for apals, aspals in gen_0(), gen_1(), gen_2():
        pals += apals
        spals += aspals
    pals.sort()
    spals.sort()
    return pals, spals

if __name__ == '__main__':
    pals, spals = gen_all()
    pairs = zip(pals, spals, caches)
    for pair in pairs:
        #print pair
        try:
            assert pair[0] == pair[2]
            assert pair[0] ** 2 == pair[1]
        except:
            print 'err:', pair
            exit()
    print 'pals =', pals
    print 'spals =', spals

