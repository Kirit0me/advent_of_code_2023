data = open("input.txt", 'r').read()
patterns = [chunk.splitlines() for chunk in data.strip().split('\n\n')]

def horizontal_mirror_line(pattern, smudges=0):
    for i, line in enumerate(pattern):
        if i + 1 == len(pattern):
            return 0
        pairs_to_check = [
            (c1, c2)
            for line1, line2 in zip(pattern[i::-1], pattern[i+1:])
            for c1, c2 in zip(line1, line2)
        ]
        if sum(1 for c1, c2 in pairs_to_check if c1 == c2) == len(pairs_to_check) - smudges:
            return i + 1

def vertical_mirror_line(pattern, smudges=0):
    transposed = list(zip(*pattern))
    return horizontal_mirror_line(transposed, smudges)

print("Part 1 : ", sum(100 * horizontal_mirror_line(pattern) + vertical_mirror_line(pattern) for pattern in patterns))
print("Part 2 : ", sum(100 * horizontal_mirror_line(pattern, 1) + vertical_mirror_line(pattern, 1) for pattern in patterns))