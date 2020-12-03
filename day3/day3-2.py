# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

#outputs an array split per line of input
def fileInput():
    f = open('day3-input.txt', 'r')
    with open('day3-input.txt') as f:
        read_data = f.read().split('\n')
    f.close()

    return read_data

def treeCounter(slope, data, startLocation, count):
    size = [len(data[0]), len(data)]
    newCount = nextLocation(startLocation, slope, data, size, count)
    return newCount


def nextLocation(location, slope, data, size, count):
    location = [(location[0] + slope[0]) % size[0], location[1] + slope[1]]
    
    # if out of bounds, end
    if (location[1] > (size[1]-1)):
        return count
    else:
        if data[location[1]][location[0]] == '#':
            count = count+1
        return nextLocation(location, slope, data, size, count)

def multiplyList(list):
    result = 1
    for i in list:
        result = result * i
    return result

if __name__ == "__main__":

    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    startLocation = [0,0]
    count = [0,0,0,0,0] #since we multiply counts for answer

    data = fileInput()

    for index, slope in enumerate(slopes):
        count[index] = treeCounter(slope, data, startLocation, count[index])

    print(multiplyList(count))
        



