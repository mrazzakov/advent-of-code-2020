# --- Part Two ---
# As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

# Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

# .......#.
# ...#.....
# .#.......
# .........
# ..#L....#
# ....#....
# .........
# #........
# ...#.....
# The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

# .............
# .L.L.#.#.#.#.
# .............
# The empty seat below would see no occupied seats:

# .##.##.
# #.#.#.#
# ##...##
# ...L...
# ##...##
# #.#.#.#
# .##.##.
# Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

# Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# #.LL.LL.L#
# #LLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLLL.L
# #.LLLLL.L#
# #.L#.##.L#
# #L#####.LL
# L.#.#..#..
# ##L#.##.##
# #.##.#L.##
# #.#####.#L
# ..#.#.....
# LLL####LL#
# #.L#####.L
# #.L####.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##LL.LL.L#
# L.LL.LL.L#
# #.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLL#.L
# #.L#LL#.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.#L.L#
# #.L####.LL
# ..#.#.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.LL.L#
# #.LLLL#.LL
# ..#.L.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
# Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

# Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()
    return read_data

def splitSeats(data):
    splitData = []
    for row in data:
        rowData = [seat for seat in row]
        splitData.append(rowData)
    return splitData

def areSeatsTaken(positions,data):
    for pos in positions:
        if data[pos[1]][pos[0]] == 'L':
            return 0
        elif data[pos[1]][pos[0]] == '#':
            return 1
    return 0
            


#size - [rows-1,cols-1]
#position - [x,y]
def countVisibleSeats(position,data):
    # [
    #     [-1,-1][0,-1][1,-1]
    #     [-1, 0][X, X][1, 0]
    #     [-1, 1][0, 1][1, 1]
    # ]
    visCount = 0

    # topLeftDiag
    visSeats = []
    x = position[0]-1
    y = position[1]-1
    while (x >= 0 and y >= 0):
        visSeats.append([x,y])
        x -= 1
        y -= 1
    visCount += areSeatsTaken(visSeats,data)

    # top
    visSeats = []
    x = position[0]
    y = position[1]-1
    while y >= 0:
        visSeats.append([x,y])
        y -= 1
    visCount += areSeatsTaken(visSeats,data)

    # topRightDiag
    visSeats = []
    x = position[0]+1
    y = position[1]-1
    while (x <= size[0] and y >= 0):
        visSeats.append([x,y])
        x += 1
        y -= 1
    visCount += areSeatsTaken(visSeats,data)

    # left
    visSeats = []
    x = position[0]-1
    y = position[1]
    while x >= 0:
        visSeats.append([x,y])
        x -= 1
    visCount += areSeatsTaken(visSeats,data)
 
    # right
    visSeats = []
    x = position[0]+1
    y = position[1]
    while x <= size[0]:
        visSeats.append([x,y])
        x += 1
    visCount += areSeatsTaken(visSeats,data)

    # botLeft
    visSeats = []
    x = position[0]-1
    y = position[1]+1
    while (x >= 0 and y <= size[1]):
        
        visSeats.append([x,y])
        x -= 1
        y += 1
    visCount += areSeatsTaken(visSeats,data)

    #bot
    visSeats = []
    x = position[0]
    y = position[1]+1
    while y <= size[1]:   
        visSeats.append([x,y])
        y += 1
    visCount += areSeatsTaken(visSeats,data)

    # botRight
    visSeats = []
    x = position[0]+1
    y = position[1]+1
    while (x <= size[0] and y <= size[1]):
        visSeats.append([x,y])
        x += 1
        y += 1
    visCount += areSeatsTaken(visSeats,data)

    return visCount


# L = Empty Seat
# # = Taken Seat
# . = Floor
# Rule 1: If seat is empty and all adjacent (up,down,left,right,all diagonals) are empty, seat is taken 
# Rule 2: If seat is taken, look if 4 or more adjacent seats are taken.  
#           - If more than 4 are taken, empty seat
#           - If less than 4 are taken, seat doesn't change
# Compare the input with the output.  If the same, END
def processSeats(data):
    newData = []
    rowCount = 0
    for row in data:
        rowData = []
        colCount = 0
        for seat in row:
            if seat != '.': #if not a floor
                visCount = countVisibleSeats([colCount,rowCount],data)
                if seat == 'L' and visCount == 0: #if rule 1 is good
                    rowData.append('#')
                elif seat == '#' and visCount < 5: #if rule 2 is good
                    rowData.append('#')
                else:
                    rowData.append('L')
            else: #if floor
                rowData.append('.')
            colCount += 1
        newData.append(rowData)
        rowCount += 1
    return newData

def countTakenSeats(data):
    seatCount = 0
    for row in data:
        for seat in row:
            if seat == '#':
                seatCount += 1
    return seatCount
            

def checkSeats(data):
    newData = processSeats(data)
    # print('-----')
    # print(newData)
    if data == newData:
        return countTakenSeats(newData)
    else:
        return checkSeats(newData)

#///////////////////////////////////////////////////
inputFile = 'day11-input.txt'

if __name__ == "__main__":
    data = fileInput()
    data = splitSeats(data)
    size = [len(data[0])-1,len(data)-1]
    seatsTaken = checkSeats(data)
    print(seatsTaken)