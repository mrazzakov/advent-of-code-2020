# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

# What is the ID of your seat?

#outputs an array split per line of input
seatRange = [64,4]
count = 0


def fileInput():
    f = open('day5-input.txt', 'r')
    with open('day5-input.txt') as f:
        read_data = f.read().split('\n')
    f.close()

    return read_data

def binaryFind(location, count, seatRange):
    if location == '':
        return count
    if (location[0] == 'B') or (location[0] == 'R'):
        count = count + seatRange
        return binaryFind(location[1:len(location)], count, int(seatRange/2))
    else:
        return binaryFind(location[1:len(location)], count, int(seatRange/2))


# BFFFBBFRRR = 70, 7, id 567
def getSeats(data):
    seatList = []
    #0-127
    for row in data:
        seat = [row[0:7],row[7:10]]
        seat[0] = binaryFind(seat[0], 0, seatRange[0])
        seat[1] = binaryFind(seat[1], 0, seatRange[1])
        seatID = seat[0] * 8 + seat[1]
        seatList.append(seatID)
    seatList.sort()  
    return seatList


def findMissingSeat(seatList):
    return [x for x in range(seatList[0],seatList[-1]+1) if x not in seatList]


if __name__ == "__main__":

   
    data = fileInput()
    seatList = getSeats(data)
    print(findMissingSeat(seatList))