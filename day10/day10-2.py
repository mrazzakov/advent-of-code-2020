# --- Part Two ---
# To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.

# The first example above (the one that starts with 16, 10, 15) supports the following arrangements:

# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
# (The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is 8.

# The second example above (the one that starts with 28, 33, 18) has many arrangements. Here are a few:

# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 46, 48, 49, (52)

# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 46, 49, (52)

# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 47, 48, 49, (52)

# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 47, 49, (52)

# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 48, 49, (52)
# In total, this set of adapters can connect the charging outlet to your device in 19208 distinct arrangements.

# You glance back down at your bag and try to remember why you brought so many adapters; there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

# What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
from math import comb
from math import ceil
from math import pow

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()
    return read_data

def convertToInts(data):
    for idx,num in enumerate(data):
        data[idx] = int(num)

def diffJoltage(data):
    data.sort()
    joltDiffList = [] 
    prevJolt = 0
    for jolt in data:
        joltDiffList.append(jolt-prevJolt)
        prevJolt = jolt
    joltDiffList.append(3) #ends with joltage of 3 everytime, easier to view flow when at end of list
    return joltDiffList

# If the one you are on is 1 and the next one is also a 1, then you can remove it
def findOptionalVals(diffData, count):
    boolList = []
    for idx,diff in enumerate(diffData):
        # print('/////',idx)
        if idx < len(diffData): #last one is always going to be 3, so skip it and one more for idx+1 
            if (diff == 1) and (diffData[idx+1] == 1):  # If the one you are on is 1 and the next one is also a 1, then you can remove it
                boolList.append(1)
                count += 1
            else:
                boolList.append(0)        
    return(boolList)

def addConsecutives(boolList):
    #Find all
    itemList = []
    itemCount = 0
    for item in boolList:
        if item == 0 and itemCount != 0:
            itemList.append(itemCount)
            itemCount = 0
        elif item == 1:
            itemCount += 1
    return itemList

def sumCombos(boolList):
    comboList = []
    count = 0
    for item in boolList:
        if item >= 3:
            k = ceil(item/2)
            total = sumNChooseK(item,k)
            comboList.append(total)
        else:
            count += item
    comboList.append(int(pow(2,count)))
    print(comboList)
    return multList(comboList)

def sumNChooseK(n,k):
    total = 0
    for num in range(k+1):
        total += comb(n,num)
    return total

def multList(inputList):
    result = 1
    for i in inputList:
        result *= i
    return result

# ///////////////////////////////////////////////////
inputFile = 'day10-input.txt'
count = 0

if __name__ == "__main__":
    data = fileInput()
    convertToInts(data)
    joltDiffList = diffJoltage(data)
    boolList = findOptionalVals(joltDiffList, count)
    itemList = addConsecutives(boolList)
    total = sumCombos(itemList)
    print(total)
    # print([joltDiffList.count(1),joltDiffList.count(2),joltDiffList.count(3)])
    # print(joltDiffList.count(1)*joltDiffList.count(3))
    # print(count)

