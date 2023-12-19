ll = [x for x in open('aoc_in18.txt').read().strip().split('\n')]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
instructions = ['R', 'D', 'L', 'U']
def run(part2):
	boundary = set()
	pos = (0, 0)
	points = [pos]
	perimeter = 0
	for l in ll:
		if part2:
			l = l.split("#")[1].split(")")[0]
			d = dirs[int(l[-1])]
			dist = int(l[:-1], 16)
		else:
			d = dirs[instructions.index(l.split(" ")[0])]
			dist = int(l.split(" ")[1])
		pos = (pos[0] + d[0] * dist, pos[1] + d[1] * dist)
		perimeter += dist
		points.append(pos)

	points = points[::-1]
	a = 0
	for i in range(len(points) - 1):
		a += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])
	print(perimeter // 2 + a // 2 + 1)

run(False)
run(True)