

from qrd import *

def test_clone():
    world = World(
'''3 3
1 1 1
1 0
1 0
1 0'''.split('\n'))
    clone = world.clone()
    assert world.__repr__() == clone.__repr__()
