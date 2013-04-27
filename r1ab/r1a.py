
if __name__ == '__main__':
    case_count = input()
    for x in xrange(0, case_count):
        E, R, N = map(int, raw_input().split(' '))
        acts = map(int, raw_input().split(' '))

        prios = [n for n in xrange(0, len(acts))]
        prios.sort(key=lambda x: -acts[x])
        
        energy = [0] * len(acts)

        def mark(index):
            e = E - energy[index]
            if e == 0: return 0
            energy[index] += e
            assert(energy[index] == E)
            i = index
            ie = E
            while i > 0:
                i -= 1
                ie -= R
                if ie <= 0:
                    break
                energy[i] = min(E, energy[i] + ie)
            i = index
            ie = E
            while i < len(acts) - 1:
                i += 1
                ie -= R
                if ie <= 0:
                    break
                energy[i] = min(E, energy[i] + ie)
            return e

        score = 0
        #print E, R
        for index in prios:
            value = acts[index]
            e = mark(index)
            score += value * e
            #print energy, 'mark index:', index, 'value:', value, 'energy:',e

        print 'Case #%d:' % (x + 1), score
