import re

with open("aoc_in1.txt", "r") as day1:
    items=day1.readlines()

# part 1

begin = 0
final = 0
arr= []
for item in items:
    for j in item:
        if(j>='0' and j<='9'):
            begin = j
            break
    for j in item:
        if(j>='0' and j<='9'):
            final = j
    # print(begin)
    # print(final)
    b = int(begin)
    f = int(final)
    b = b*10
    # print(b)
    # print(f)
    arr.append(b + f)

print("first part : " + str(sum(arr)))

# part 2

arr2 = []

for item in items: 
    item = item.replace("zero", "z0ero")
    item = item.replace("one", "o1ne")
    item = item.replace("two", "t2wo")
    item = item.replace("three", "t3hree")
    item = item.replace("four", "f4our")
    item = item.replace("five", "f5ive")
    item = item.replace("six", "s6ix")
    item = item.replace("seven", "s7even")
    item = item.replace("eight", "e8ight")
    item = item.replace("nine", "n9ine")
    for j in item:
        if(j>='0' and j<='9'):
            begin = j
            break
    for j in item:
        if(j>='0' and j<='9'):
            final = j
    # print(begin)
    # print(final)
    b = int(begin)
    f = int(final)
    b = b*10
    # print(b)
    # print(f)
    arr2.append(b + f)

print("Second part : " + str(sum(arr2)))



