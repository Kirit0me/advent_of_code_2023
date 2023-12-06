from math import sqrt
time = [41, 77, 70, 96]
distance = [249, 1362, 1127, 1011]

total = []
for i in range(len(time)):
    ways = []
    for j in range(time[i]):
        if (time[i]-j)*j > distance[i]:
            ways.append(j)
    total.append(len(ways))

print(total)

# part 2

time2 = 41777096
distance2 = 249136211271011

# time2 = 71530
# distance2 = 940200

# arr = []
start = int((-time2 - sqrt(time2*time2 - 4*distance2))/2)
end = int((-time2 + sqrt(time2*time2 - 4*distance2))/2)
renge = abs(start - end)
print(renge)
# for k in range(renge):
#     print(k/renge)
#     if (time2-k)*k > distance2:
#         arr.append(k)
# print(arr)
# print(arr.pop())
# print(len(arr))

