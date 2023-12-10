import time
from functools import reduce

t1 = time.time()
items = open('aoc_in5.txt').read().split('\n\n')
seeds = items[0]
maps = items[1:]

def lookup(val, m):
    ranges = m.split('\n')[1:]
    for r in ranges:
        dst, src, n = map(int, r.split())
        if src <= val < src+n:
            return val-src+dst
    else: return val
print(min(reduce(lookup, maps, int(s)) for s in seeds.split()[1:]))
t2 = time.time()
print(t2-t1)

# part 2

t3 = time.time()
for s in seeds.split()[1:]:
    i = 0
    se = int(s) * 2
    renge = int(s) * 2 + 1
    values_to_reduce = [reduce(lookup, maps, se + i) for i in range(renge)]
    print(i/10)
    i = i + 1
    print(min(values_to_reduce))
t4 = time.time()
print(t4-t3)

