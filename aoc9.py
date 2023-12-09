def find_differences(values):
    while True:
        cur = values[-1]
        next = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        values.append(next)
        if all(number == 0 for number in next):
            break

def extrapolate(values:list):
    values[-1].append(0)
    values[-1].insert(0, 0)
    for i in range(len(values) - 2, -1, -1):
        values[i].append(values[i][-1] + values[i + 1][-1])
        values[i].insert(0, values[i][0] - values[i + 1][0])

with open("aoc_in9.txt") as file:
    sum_extrapolated1 = 0
    sum_extrapolated2 = 0
    for row in file:
        values = [[int(number) for number in row.split()]]
        find_differences(values)
        extrapolate(values)
        sum_extrapolated1 += values[0][-1]
        sum_extrapolated2 += values[0][0]
    print(sum_extrapolated1)
    print(sum_extrapolated2)