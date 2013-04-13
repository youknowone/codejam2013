
from math import sqrt, ceil, trunc

from paldic import pals, spals

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

def fairsquare_slow(start, end):
    qstart = int(ceil(sqrt(start)))
    qend = trunc(sqrt(end))
    #print start, end, '------------'
    c = 0
    for rt in xrange(qstart, qend + 1):
        if is_palindrome(rt) and is_palindrome(rt**2):
            c += 1
            #print rt, rt**2
    return c

def fairsquare_cached(start, end):
    qstart = int(ceil(sqrt(start)))
    qend = trunc(sqrt(end))

    sstart = get_seed1(str(qstart))
    send = get_seed2(str(qend))
    c = 0
    #print start, end, '------------'
    gen_pal2 = gen_palindrome2
    endian = long(send) + 1
    seed = long(sstart)
    while True:
        sseed = str(seed)
        pal = int(gen_palindrome1(sseed))
        if pal > qend:
            break
        if qstart <= pal:
            if is_palindrome(pal ** 2):
                #print pal, pal ** 2
                c += 1
        pal = int(gen_pal2(sseed))
        if pal > qend:
            gen_pal2 = lambda x: 0
        elif qstart <= pal:
            if square_is_palindrome(pal):
                #print pal, pal ** 2
                c += 1
        seed += 1
    return c

def fairsquare(start, end):
    count = 0
    for spal in spals:
        if spal > end:
            break
        if start <= spal <= end:
            count += 1
    return count

if __name__ == '__main__':
    count = input()
    for x in xrange(1, count + 1):
        start, end = map(int, raw_input().split(' '))
        count = fairsquare(start, end)
        print 'Case #%d:' % x, count

