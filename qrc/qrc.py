
from math import sqrt, ceil, trunc

from paldic import pals, spals

def fairsquare_slow(start, end):
    from gen_paldic import is_palindrome
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
    from gen_paldic import is_palindrome
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

