
import copy
from collections import OrderedDict

class Chest(object):
    def __init__(self, line):
        nums = map(int, line.split(' '))
        self.keytype = nums[0]
        self.keys = nums[2:]
        assert nums[1] == len(self.keys)

    def __repr__(self):
        return '<Chest({},{})>'.format(self.keytype, self.keys)

class World(object):
    def __init__(self, lines=None):
        if not lines:
            return
        self.keycount, self.chestcount = map(int, lines[0].split(' '))
        self.keys = map(int, lines[1].split(' '))
        self.chests = [Chest(line) for line in lines[2:]]
        assert len(self.keys) == self.keycount
        assert len(self.chests) == self.chestcount
        cdic = OrderedDict()
        for chest in self.chests:
            try:
                cdic[chest.keytype].append(chest)
            except KeyError:
                cdic[chest.keytype] = [chest]
        for chestlist in cdic.values():
            chestlist.sort(key=lambda chest: -len(chest.keys))
        self.chestdic = OrderedDict(sorted(cdic.iteritems(), 
                                    key=lambda (key, chests): -sum(
                                        map(lambda chest: len(chest.keys), chests)
                                    )))

    def __repr__(self):
        return '<World(keys{},chests{{{}}})>'.format(self.keys, ','.join([(str(k) + ': ' + str(v)) for k, v in self.chestdic.iteritems()]))

    def clone(self):
        new = World()
        new.keys = copy.deepcopy(self.keys)
        new.chestdic = copy.deepcopy(self.chestdic)
        return new

def solve(world):
    clone = world.clone()


if __name__ == '__main__':
    count = input()
    for xx in xrange(0, count):
        lines = [raw_input(), raw_input()]
        keycount, chestcount = map(int, lines[0].split(' '))
        lines += [raw_input() for x in xrange(0, chestcount)]
        world = World(lines)
        print world 