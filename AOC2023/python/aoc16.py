mirror_grid = open("aoc_in16.txt", 'r').read().split("\n")

moves = {
    "N": {
        ".": "N",
        "-": "EW",
        "|": "N",
        "/": "E",
        "\\": "W",
    },
    "E": {
        ".": "E",
        "-": "E",
        "|": "NS",
        "/": "N",
        "\\": "S",
    },
    "S": {
        ".": "S",
        "-": "EW",
        "|": "S",
        "/": "W",
        "\\": "E"
    },
    "W": {
        ".": "W",
        "-": "W",
        "|": "NS",
        "/": "S",
        "\\": "N",
    }
}

directions = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}


def solve(matrix, start):
    n = len(matrix)
    m = len(matrix[0])

    queue = [start]
    visited = set()
    while queue:
        new_queue = []
        for i, j, d in queue:
            di, dj = directions[d]
            ni, nj = i + di, j + dj
            if not 0 <= ni < n:
                continue
            if not 0 <= nj < m:
                continue

            for nd in moves[d][matrix[ni][nj]]:
                if (ni, nj, nd) in visited:
                    continue
                visited.add((ni, nj, nd))
                new_queue.append((ni, nj, nd))
        queue = new_queue
    return len({(i, j) for i, j, d in visited})


matrix = list(map(list,mirror_grid))

start = (0, -1, "E")
print(solve(matrix, start))

# part 2

n = len(matrix)
m = len(matrix[0])

starts = []
starts += [(i, -1, 'E') for i in range(n)]
starts += [(i,  m, 'W') for i in range(n)]
starts += [(-1, j, 'S') for j in range(m)]
starts += [(n,  j, 'N') for j in range(m)]

print(max(solve(matrix, start) for start in starts))

