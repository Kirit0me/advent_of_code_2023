universe = open("aoc_in11.txt", 'r').read().split("\n")

length = len(universe)
width = len(universe[0])

empty_rows = []
empty_columns = []
galaxies = []

for i in range(length):
    empwid = True
    emplen = True
    for j in range(width):
        if(universe[j][i]!='.'):
            emplen = False
        if(universe[i][j]!='.'):
            empwid = False
        if(universe[i][j] == '#'):
            galaxies.append([i, j])    
    if empwid:
        empty_rows.append(i)
    if emplen:
        empty_columns.append(i)
print("Number of columns : ", empty_columns)
print("Number of rows : ", empty_rows)
print(galaxies)
visited = []
distance = []
count = 0
for i in galaxies:
    col_add = 0
    row_add = 0
    for j in range(len(empty_columns)):
        if i[1]-empty_columns[j] > 0:
            col_add+=1
        
    for k in range(len(empty_rows)):
        if i[0]-empty_rows[k] > 0:
            row_add+=1
    
    # i[1]+=col_add part 1
    # i[0]+=row_add part 1
    i[1]+=(999_999*col_add)
    i[0]+=(999_999*row_add)

for galaxy in galaxies:
    visited.append(galaxy)
    
    for to_galaxy in galaxies:
        if to_galaxy not in visited:
            row_dist = abs(galaxy[1]-to_galaxy[1])
            col_dist = abs(galaxy[0]-to_galaxy[0])
            distance.append(row_dist + col_dist)

print(galaxies)
print( sum(distance))
