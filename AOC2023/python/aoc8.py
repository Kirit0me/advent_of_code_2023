from math import lcm

instructions = "LRRLRRLRRLRRRLRRLRRRLRRLRRRLRLRLLRLRLRRLLLRLRLRRRLRRLRLRRRLRRLRRLRRLLLRRLRRRLRRRLRLLRRLRLLRRLRRRLRRLRLRRRLRLRLRRLRLRRRLLRRRLLRRRLRLRRRLRRLLRRLRRRLRRLRRLLRRLRRLRRRLLLRRRLRRLRRLRRLRLRRRLRRLLLLRLRRLRRRLRLLRRLRLLRRLRRRLRRRLRRRLLRRLRRLRRLRRRLRRLRRRLLRLRRRLRRRLRRRLLRRRLRRLRRRR"
# instructions = "LR"
input = open("aoc_in8.txt", 'r').read().split("\n")
place = {}

for i in range(len(input)):
    a, b, c, d = input[i].split()
    if a not in place.keys():
        place[a] = (c, d)

count = 0

# part 1

k = "AAA"
pointer = place[k]
while(k != "ZZZ"):
    print(k)
    print(instructions[count%len(instructions)])
    if(instructions[count%len(instructions)] == "L"):
        k = pointer[0]
        pointer = place[k]
        count += 1
        
    elif(instructions[count%len(instructions)] == "R"):
        k = pointer[1]
        pointer = place[k]
        count += 1

print("part 1: ", count)

# part 2

# def check_reached(dest):
#     if dest == []:
#         return False
#     for i in range(len(dest)):
#         if dest[i][2] != "Z":
#             return False
#     return True

# src = []
# dest = []
# count2 = 0
# for i in place.keys():
#     if(i[2] == "A"):
#         src.append(i)
# print(src)
# while not check_reached(dest):
#     print(src, dest, count2)
#     if(instructions[count2%len(instructions)] == "L"):
#         dest = []
#         for i in src:
#             dest.append(place[i][0])
#         src = dest
#         count2+=1
#     elif(instructions[count2%len(instructions)] == "R"):
#         dest = []
#         for i in src:
#             dest.append(place[i][1])
#         src = dest
#         count2+=1

# Not brute force Part 2

src = []
count_t = []
for i in place.keys():
    if(i[2] == "A"):
        src.append(i)
print(src)
for i in src:
    acc = 0
    k2 = i
    print(i)
    pointer2 = place[k2]
    while(k2[2] != "Z"):
        if(instructions[acc%len(instructions)] == "L"):
            k2 = pointer2[0]
            pointer2 = place[k2]
            acc += 1
            
        elif(instructions[acc%len(instructions)] == "R"):
            k2 = pointer2[1]
            pointer2 = place[k2]
            acc += 1
    count_t.append(acc)
print(count_t)
print("part 2 : ", lcm(*count_t))