with open("aoc_in2.txt", "r") as day2:
    items=day2.readlines()
arr = []
for i in range(len(items)): 
    total_games = items[i].split(":")
    game = total_games[1]
    valid = True
    games = game.split(";")
    for g in games:
        the_game = g.split(",")
        for tg in the_game:
            t = tg.split(" ")
            if(int(t[1]) > 12 and (t[2] == 'red' or t[2] == 'red\n')):
                valid = False
            if(int(t[1]) > 13 and (t[2] == 'green' or t[2] == 'green\n')):
                valid = False
            if(int(t[1]) > 14 and (t[2] == 'blue' or t[2] == 'blue\n')):
                valid = False
    if valid:
        arr.append(i + 1)
    
print(sum(arr))

# part 2

arr2 = []
for i in range(len(items)): 
    total_games = items[i].split(":")
    game = total_games[1]
    games = game.split(";")
    tred = 0
    tgreen = 0
    tblue = 0
    for g in games:
        the_game = g.split(",")
        for tg in the_game:
            print(tg)
            colors = tg.split(" ")
            if(colors[2] == 'red' or colors[2] == 'red\n'):
                if(tred < int(colors[1])):
                    tred = int(colors[1])
                    print(tred)
            
            if(colors[2] == 'green' or colors[2] == 'green\n'):
                if(tgreen < int(colors[1])):
                    tgreen = int(colors[1])
                    print(tgreen)
            
            if(colors[2] == 'blue' or colors[2] == 'blue\n'):
                if(tblue < int(colors[1])):
                    tblue = int(colors[1])
                    print(tblue)
    total = tred*tgreen*tblue
    arr2.append(total)        

print(sum(arr2))