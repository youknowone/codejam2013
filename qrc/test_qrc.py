
import pytest
from qrc import *
from gen_paldic import *

@pytest.mark.parametrize(('n', 'r'), [
    [1, True],
    [4, True],
    [10, False],
    [131, True],
    [100, False],
    [99, True],
])
def test_palindrome(n, r):
    assert is_palindrome(n) == r

@pytest.mark.parametrize(('n', 'p1', 'p2'), {
    (1, 1, 11),
    (12, 121, 1221),
    (50, 505, 5005),
})
def test_gen_palindrome(n, p1, p2):
    assert gen_palindrome1(str(n)) == str(p1)
    assert gen_palindrome2(str(n)) == str(p2)

@pytest.mark.parametrize(('start', 'end', 'c'), [
    (1, 4, 2),
    (10, 120, 0),
    (100, 1000, 2),
    (21, 584, 2),
    (21, 484, 2),
])
def test_fairsquare(start, end, c):
    assert fairsquare_slow(start, end) == c
    assert fairsquare(start, end) == c

@pytest.mark.parametrize(('n', 's1', 's2'), [
    (1, 1, 9),
    (11, 1, 9),
    (12, 1, 9),
    (100, 10, 99),
    (1234, 10, 99),
])
def test_seed(n, s1, s2):
    assert get_seed1(str(n)) == str(s1)
    assert get_seed2(str(n)) == str(s2)

