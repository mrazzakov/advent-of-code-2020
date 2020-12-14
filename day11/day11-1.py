# --- Day 11: Seating System ---
# Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

# By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

# The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

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
# Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.

# After one round of these rules, every seat in the example layout becomes occupied:

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
# After a second round, the seats with four or more occupied adjacent seats become empty again:

# #.LL.L#.##
# #LLLLLL.L#
# L.L.L..L..
# #LLL.LL.L#
# #.LL.LL.LL
# #.LLLL#.##
# ..L.L.....
# #LLLLLLLL#
# #.LLLLLL.L
# #.#LLLL.##
# This process continues for three more rounds:

# #.##.L#.##
# #L###LL.L#
# L.#.#..#..
# #L##.##.L#
# #.##.LL.LL
# #.###L#.##
# ..#.#.....
# #L######L#
# #.LL###L.L
# #.#L###.##
# #.#L.L#.##
# #LLL#LL.L#
# L.L.L..#..
# #LLL.##.L#
# #.LL.LL.LL
# #.LL#L#.##
# ..L.L.....
# #L#LLLL#L#
# #.LLLLLL.L
# #.#L#L#.##
# #.#L.L#.##
# #LLL#LL.L#
# L.#.L..#..
# #L##.##.L#
# #.#L.LL.LL
# #.#L#L#.##
# ..L.L.....
# #L#L##L#L#
# #.LLLLLL.L
# #.#L#L#.##
# At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?


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

#size - [rows-1,cols-1]
#position - [x,y]
def listAdjSeats(position):
    # [
    #     [-1,-1][0,-1][1,-1]
    #     [-1, 0][X, X][1, 0]
    #     [-1, 1][0, 1][1, 1]
    # ]
    x = position[0]
    y = position[1]
    allAdjSeats = [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    adjSeats = []

    for location in allAdjSeats:  
        if (0 <= location[0] <= size[0]) and (0 <= location[1] <= size[1]):
            adjSeats.append(location)
    return adjSeats

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
                adjCount = 0
                adjSeats = listAdjSeats([rowCount,colCount])
                for adjSeat in adjSeats:
                    if data[adjSeat[0]][adjSeat[1]] == '#':
                        adjCount += 1
                if seat == 'L' and adjCount == 0: #if rule 1 is good
                    rowData.append('#')
                elif seat == '#' and adjCount < 4: #if rule 2 is good
                    rowData.append('#')
                else:
                    rowData.append('L')
                # print(adjCount,'[',rowCount,colCount,']', adjSeats)
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
    # print('------')
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
    size = [len(data)-1,len(data[0])-1]
    seatsTaken = checkSeats(data)
    print(seatsTaken)
    
