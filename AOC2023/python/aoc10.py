grid = open("aoc_in10.txt", 'r').read().split("\n")

width = len(grid[0])
height = len(grid)

data = ''.join(grid)

dmap = {
    'S': [],
    '|': [width, -width],
    '-': [-1, 1],
    '.': [],
    '7': [-1, width],
    'L': [1, -width],
    'J': [-1, -width],
    'F': [1, width]
}

start = data.find('S')
path = {start}
data = [dmap[c] for c in data]

for i, offsets in enumerate(data):
    if start in (i + o for o in offsets):
        dmap['S'].append(i - start)

print(dmap)

dist = 0
nodes = None
while True:
    temp = nodes
    nodes = set()
    for p in (temp or path):
        for offset in data[p]:
            if p + offset not in path:
                nodes.add(p + offset)
    if nodes:
        path |= nodes
        dist += 1
    else:
        break
print(dist)

# part 2

dots = 0
dots_inside = 0
for i in range(len(data)):
    if i in path:
        continue
    else:
        dots+=1
    out_left = True
    out_right = True
    # out_top = True
    # out_bot = True
    j = i
    while j > 0:
        if j in path and 1 in data[j]:
            out_right = not out_right
        if j in path and -1 in data[j]:
            out_left = not out_left
        
        j -= width
    if not (out_left or out_right):
        dots_inside+=1

print("Total spaces : ", dots)
print("Total inside loop : ", dots_inside)
