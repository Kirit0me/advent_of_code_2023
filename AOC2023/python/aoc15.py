import collections as co

inits = open("aoc_in15.txt", 'r').read().split(",")

sums = []

def hashy_dashy(s):
    count = 0
    for i in s:
        count += ord(i)
        count *= 17
        count %= 256
    return count
for init in inits:
    c = hashy_dashy(init)
    sums.append(c)

print("Part 1 : ", sum(sums))

boxes: co.defaultdict[int, co.OrderedDict[str, int]] = co.defaultdict(co.OrderedDict)
for init in inits:
    if init.endswith('-'):
        label = init.removesuffix("-")
        boxes[hashy_dashy(label)].pop(label, None)
    else:
        label, n = init.split("=")
        boxes[hashy_dashy(label)][label] = int(n)

print("Part 2 : ", sum((b + 1) * (i + 1) * n
        for b, box in boxes.items()
        for i, n in enumerate(box.values())))