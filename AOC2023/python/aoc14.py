mirror = open("aoc_in14.txt", 'r').read().split()
h = len(mirror)
w = len(mirror)

loads = []
for i in range(w):
    rocks = 0
    load = 0
    for j in range(h-1, -1, -1):
        if(mirror[j][i] == "#"):
            for k in range(rocks):
                load += (h-j-k-1)
            rocks = 0
        if(mirror[j][i] == "O"):
            rocks += 1
    for k in range(rocks):
        load += (h-j-k)
        rocks = 0
    loads.append(load)

print("Part 1 : ", sum(loads))

# part 2

grid = list(map(list,mirror))
print(grid)

def slide(grid):
    for j in range(h):
        ci = 0
        for i in range(w):
            if grid[i][j] == "#":
                ci = i + 1
            if grid[i][j] == "O":
                grid[i][j] = "."
                grid[ci][j] = "O"
                ci += 1

def get_score(grid):
    ans = 0
    for i in range(h):
        ans += (h - i) * grid[i].count("O")
    return ans

def rotate(grid):
    new_grid = [["." for j in range(h)] for i in range(w)]
    for i in range(h):
        for j in range(w):
            new_grid[j][h - i - 1] = grid[i][j]
    return new_grid

def to_str(grid):
    return "".join(["".join(grid[i]) for i in range(len(grid))])

d = {}
goal = 1000000000
idx = 1
while True:
    for j in range(4):
        slide(grid)
        grid = rotate(grid)
    x = to_str(grid)
    if x in d:
        cyclen = idx - d[x][0]
        for a,b in d.values():
            if a >= d[x][0] and a % cyclen == goal % cyclen:
                print(b)
        break
    d[x] = (idx, get_score(grid))
    idx += 1


