

from qrd import *

def test_chestclone():
    for c in '1 1 1', '1 3 1 2 3':
        chest = Chest(c)
        clone = chest.clone()
        assert chest.__repr__() == clone.__repr__()
        chest.keys.remove(1)
        assert chest.__repr__() != clone.__repr__()

def test_clone():
    world = World(
'''3 3
1 1 1
1 0
1 0
1 0'''.split('\n'))
    clone = world.clone()
    assert world.__repr__() == clone.__repr__()
    clone.chestdic[1][0].keys.append(10)
    clone.keys.remove(1)
    assert world.__repr__() != clone.__repr__()
