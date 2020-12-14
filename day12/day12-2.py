# --- Part Two ---
# Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

# Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal to the given value.
# The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

# For example, using the same instructions as above:

# F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
# N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
# F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
# R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
# F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
# After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

# Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()
    return read_data

def splitData(data):
    newData = []
    for line in data:
        newData.append([line[0],int(line.lstrip("NSEWLRF"))])
    return newData

# location = [x,y]
def moveNorth(location,distance):
    return [location[0],location[1]-distance]

def moveSouth(location,distance):
    return [location[0],location[1]+distance]

def moveEast(location,distance):
    return [location[0]+distance,location[1]]

def moveWest(location,distance):
    return [location[0]-distance,location[1]]

# https://calcworkshop.com/transformations/rotation-rules/#:~:text=90%20Degree%20Rotation,y%20and%20make%20y%20negative.
def rotateLeft(location,angle):
    #Y axis is flipped
    location = [location[0],-location[1]]
    #could be a while loop, but this is easier to read
    if angle % 360 == 0:
        return [location[0],-location[1]]
    elif angle % 360 == 90:
        return [-location[1],-location[0]]
    elif angle % 360 == 180:
        return [-location[0],location[1]]
    else:
        return [location[1],location[0]]
    

# https://calcworkshop.com/transformations/rotation-rules/#:~:text=90%20Degree%20Rotation,y%20and%20make%20y%20negative.
def rotateRight(location,angle):
    return rotateLeft(location,(-angle % 360))


def moveForward(shipLoc,waypointLoc,distance):
    newShipX = shipLoc[0] + (distance * waypointLoc[0])
    newShipY = shipLoc[1] + (distance * waypointLoc[1])
    return [newShipX,newShipY]

def processData(data,position,waypoint):
    if len(data) == 0:
        return position
    else:
        insLet = data[0][0]
        insNum = data[0][1]
        print(insLet,insNum,position,waypoint)
        if insLet == 'N':
            waypoint = moveNorth(waypoint,insNum)
        elif insLet == 'S':
            waypoint = moveSouth(waypoint,insNum)
        elif insLet == 'E':
            waypoint = moveEast(waypoint,insNum)
        elif insLet == 'W':
            waypoint = moveWest(waypoint,insNum)
        elif insLet == 'L':
            waypoint = rotateLeft(waypoint,insNum)
        elif insLet == 'R':
            waypoint = rotateRight(waypoint,insNum)
        else:
            position = moveForward(position,waypoint,insNum)
        data.pop(0)
        return processData(data,position,waypoint)
    
    


#///////////////////////////////////////////////////
inputFile = 'day12-input.txt'

if __name__ == "__main__":
    data = fileInput()
    data = splitData(data)
    endLocation = processData(data,[0,0],[10,-1])
    print(endLocation)
    print(abs(endLocation[0]) + abs(endLocation[1]))

    
