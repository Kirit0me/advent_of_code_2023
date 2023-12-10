with open("aoc_in3.txt", "r") as day3:
    items=day3.readlines()


def magic(numList):
    if(numList == []):
        return -1           
    s = map(str, numList)   
    s = ''.join(s)          
    s = int(s)              
    return s

arr = []
for k in range(len(items)):
    isNum = False
    num = []
    length = 0
    for i in range(len(items[k])):
        if(items[k][i].isdigit()):
            isNum = True
            num.append(int(items[k][i]))
            length+=1
            # print(num)
        else:
            if(isNum):
                # print(length)
                number = magic(num)
                start = i-length
                end = i
                
                if items[k][start-1] != '.' or items[k][end] != '.' :
                    arr.append(number)
                else:
                    for j in range(start - 1, end + 1):
                        if items[(k + 1) % len(items)][j % len(items[k])] != '.' or items[k - 1][j % len(items[k])] != '.':
                            if not (items[k + 1][j].isdigit() or items[k - 1][j].isdigit()):
                                arr.append(number)
                                break
                num = []
                length = 0
                isNum = False
# print(arr)
print(sum(arr))

# part 2
arr2 = []
pos = []

for k in range(len(items)):
    isNum = False
    num = []
    length = 0
    for i in range(len(items[k])):
        if(items[k][i].isdigit()):
            isNum = True
            num.append(int(items[k][i]))
            length+=1
        else:
            if(isNum):
                number = magic(num)
                start = i-length
                end = i
                
                if items[k][start-1] == '*' or items[k][end] != '*' :
                    arr2.append(number)
                    pos.append([start, k])
                else:
                    for j in range(start - 1, end + 1):
                        if items[(k + 1) % len(items)][j % len(items[k])] == '*' or items[k - 1][j % len(items[k])] == '*':
                            arr2.append(number)
                            pos.append([start, k])
                            break
                num = []
                length = 0
                isNum = False

new_pos = []
for 
# for n in range(len(arr2)):
#     print(n, ". ", arr2[n], " is at ", pos[n])
