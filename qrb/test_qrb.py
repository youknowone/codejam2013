
import pytest
from qrb import *

@pytest.mark.parametrize(('input',), [
('''
3 3
2 1 2
1 1 1
2 1 2
''',),
]) 
def test_field(input):
    lgen = l for l in input.split('\n')
    lgen.next() #newln
    y, x = lgen.next().split()
    
        if l == '': continue

    assert False
