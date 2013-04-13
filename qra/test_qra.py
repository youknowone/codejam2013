
from qra import *

def test_line():
    for c, l, r in [
        ('X','XXXT',True),
        ('O','XOXT',False),
        ('O','XXOO',False),
        ('O','OXOX',False),
        ('O','XXOO',False),
    ]:
        assert check_line(c, l) == r

def test_crossv():
    for data, v1, v2 in [
        (['XXXO', '..O.', '.O..', 'T...'], 'X...', 'OOOT'),
    ]:
        tttt = TTTT(data)
        assert cross1(data) == v1
        assert cross2(data) == v2

def test_cross():
    for c, data, result in [
        ('O', ['XXXO', '..O.', '.O..', 'T...'], True),
    ]:
        tttt = TTTT(data)
        r1 = check_cross1(c, data)
        r2 = check_cross2(c, data)
        assert r1 or r2 == result

def test_lines():
    for c, data, result in [
        ('X', ['XXXT', '....', 'OO..', '....'] , True),
        ('X', ['XOXT', 'XXOO', 'OXOX', 'XXOO'], False),
        ('O', ['XOXT', 'XXOO', 'OXOX', 'XXOO'], False),
        ('X', ['XXXO', '..O.', '.O..', 'T...'], False),
        ('O', ['XXXO', '..O.', '.O..', 'T...'], True),
    ]:
        tttt = TTTT(data)
        assert check_lines(c, data) == result

def test_tttt():
    for data, result in [
        (['XXXT', '....', 'OO..', '....'] , 'X won'),
        (['XOXT', 'XXOO', 'OXOX', 'XXOO'], 'Draw'),
        (['XXXO', '..O.', '.O..', 'T...'], 'O won'),
    ]:
        tttt = TTTT(data)
        print tttt
        assert tttt.statement() == result
