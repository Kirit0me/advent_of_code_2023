with open("aoc_in4.txt", "r") as day4:
    items=day4.readlines()
arr = []
for i in range(len(items)): 
    the_game = items[i].split(":")
    games = the_game[1].split("|")
    conditions = games[0].split()
    rounds = games[1].split()
    wins = []
    for r in rounds:
        if r in conditions:
            wins.append(r)
    if(wins):
        power = len(wins) - 1
        points = 2**power
    else:
        points = 0
    print(power)
    print(points)
    arr.append(points)

print(sum(arr))

# part 2

scratch = [0] * (len(items)+1)
for i in range(len(items)): 
    the_game = items[i].split(":")
    games = the_game[1].split("|")
    conditions = games[0].split()
    rounds = games[1].split()
    j = i+1
    scratch[i+1] += 1
    for r in rounds:
        if r in conditions:
            j = j+1
            scratch[j]+=(1* scratch[i+1] )
    
    print(scratch)
print(sum(scratch))
    
    