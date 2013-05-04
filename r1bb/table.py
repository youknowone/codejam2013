

dtable = {}
table = [0]
summ = 0
for i in xrange(0, 10):
    add = 4 * i + 1
    summ += add
    dtable[i] = summ
    while len(table) < summ:
        table.append(i)
    if summ > 1000000:
        break
print table
print dtable
for i, k in enumerate(dtable):
    print i, k, dtable[k], table[k]
    assert table[k] == dtable[k]