#Random for island generation.
import random

columns = []

for column in range(10):
    this_row = []
    for row in range(10):
        #25% chance for any given 
        if random.randint(0,20) < 5:
            this_row.append("1")
        else:
            this_row.append("0")
    columns.append(this_row)

#Print the grid.
for column in columns:
    print(" ".join(column))

#Function to return the coordinates of ajacent island squares.
def check_adjacent(x,y):
    adjacent = []
    #If the square to the left is an islands, add its coords, and so on.
    try:
        if columns[x-1][y] == "1" and copy[x-1][y] != "*":
            adjacent.append([x-1,y])
    except:
        #If there is no index (the island is on the edge), pass.
        pass
    try:
        if columns[x+1][y] == "1" and copy[x+1][y] != "*":
            adjacent.append([x+1,y])
    except:
        pass
    try:
        if columns[x][y+1] == "1" and copy[x][y+1] != "*":
            adjacent.append([x,y+1])
    except:
        pass
    try:
        if columns[x][y-1] == "1" and copy[x][y-1] != "*":
            adjacent.append([x,y-1])
    except:
        pass
    #Repeat, but with diagonals.
    try:
        if columns[x+1][y+1] == "1" and copy[x+1][y+1] != "*":
            adjacent.append([x+1,y+1])
    except:
        pass
    try:
        if columns[x+1][y-1] == "1" and copy[x+1][y-1] != "*":
            adjacent.append([x+1,y-1])
    except:
        pass
    try:
        if columns[x-1][y+1] == "1" and copy[x-1][y+1] != "*":
            adjacent.append([x-1,y+1])
    except:
        pass
    try:
        if columns[x-1][y-1] == "1" and copy[x-1][y-1] != "*":
            adjacent.append([x-1,y-1])
    except:
        pass
    #Return the coordinates of ALL adjacent island tiles.
    return adjacent

#Keep track of amount of islands.
islands = 0

#A copy we can replace islands we've already checked in.
copy = columns

for column in range(len(columns)):
    for this_square in range(len(columns[column])):
        #If this square is not an edge, and is not an already-checked island:
        if copy[column][this_square] != "*":
            #If the square is in the first or last row or column, then it is an edge square and must we water.
            if column == len(columns)-1 or column == 0 or this_square == 0 or this_square == len(columns[column])-1:
                #Replace these squares with *, so we can ignore them in future processing.
                copy[column][this_square] = "*"
            #If it is not an edge square, check if it's an island, and hasn't already been checked.
            elif columns[column][this_square] == "1" and copy[column][this_square] != "*":
                islands += 1
                #Set the initial square of a found island to be ignored.
                copy[column][this_square] = "*"
                #Keeps track of whether the entire island has been found.
                found_whole_island = False
                #All the coordinates in an island.
                this_island = check_adjacent(column,this_square)
                while found_whole_island == False:
                    for coords in this_island:
                        #If we find coordinates in an islands, set them to * so they can be ignored.
                        copy[coords[0]][coords[1]] = "*"
                        next_set = check_adjacent(coords[0],coords[1])
                        #Check the adjacent tiles of every square in the island.
                        for pair in next_set:
                            this_island.append(pair)
                    #Innocent until proven guilty strategy to check if every square in the island
                    #has been found and checked.
                    done_yet = True
                    for coords in this_island:
                        if copy[coords[0]][coords[1]] != "*":
                            done_yet = False
                    if done_yet:
                        found_whole_island = True

#Output the island count.    
print("\nIsland count: %s" % islands)
#Format the grid properly, so us humans can check it properly.
for copy_column in range(len(copy)):
    for copy_row in range(len(copy[copy_column])):
        if copy_row != 0 and copy_row != len(copy[copy_column])-1 and copy_column != 0 and copy_column != len(copy)-1:
            if copy[copy_column][copy_row] == "*":
                copy[copy_column][copy_row] = "1"
action = input("[H]ide edges?\n> ")
#Print the formatted version if they ask for it!
if action.lower()[0] == "h":
    for column in copy:
        print(" ".join(column))
    
            
    
