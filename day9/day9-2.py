# --- Part Two ---
# The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

# Again consider the above example:

# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

# To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

# What is the encryption weakness in your XMAS-encrypted list of numbers?
import sys
sys.setrecursionlimit(10000)

inputFile = 'day9-input.txt'
size = 25

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()
    return read_data

def convertToInts(data):
    for idx,num in enumerate(data):
        data[idx] = int(num)

def makePreamble(data,size):
    preamble = []
    for i in range(size):
        preamble.append(data[0])
        fullList.append(data[0])
        data.pop(0)
    return preamble

def isNumSum(preamble,nextNum):
    for i in preamble:
        for j in preamble:
            if i == j: #assume numbers in preamble can not be the same
                continue
            elif (i + j) == nextNum:
                return True
    return False

def updatePreambleData(preamble,data):
    preamble.append(data[0])
    fullList.append(data[0])
    data.pop(0)
    preamble.pop(0)

def findFirstErr(preamble,data):
    if isNumSum(preamble,data[0]):
        updatePreambleData(preamble,data)
        return findFirstErr(preamble,data)
    else:
        return data[0]

#if sum is less than number, add next number to list
#if sum is greater than number, subtract fist number in list
#if sum IS number, return list
def continguousSum(contList,fullList,errNum,idx):
    total = sum(contList)
    print(total,':',errNum)

    if total < errNum:
        contList.append(fullList[idx])
        return continguousSum(contList,fullList,errNum,idx+1)
    elif total > errNum:
        contList.pop(0)
        return continguousSum(contList,fullList,errNum,idx)
    else:
        return contList


#///////////////////////////////////////////////////
fullList = []

if __name__ == "__main__":
    data = fileInput()
    convertToInts(data)
    preamble = makePreamble(data,size)
    errNum = findFirstErr(preamble,data)
    contSet = continguousSum([],fullList,errNum,0)
    encryptWk = min(contSet) + max(contSet)
    print(min(contSet),max(contSet))
    print(encryptWk)