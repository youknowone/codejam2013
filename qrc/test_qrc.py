
import pytest
from qrc import *

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

@pytest.mark.parametrize(('start', 'end', 'c'), [
    (1, 4, 2),
    (10, 120, 0),
    (100, 1000, 2),
])
def test_fairsquare(start, end, c):
    assert fairsquare(start, end) == c