# --- Part Two ---
# For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

# A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

# If the bitmask bit is 0, the corresponding memory address bit is unchanged.
# If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
# If the bitmask bit is X, the corresponding memory address bit is floating.
# A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

# For example, consider the following program:

# mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# When this program goes to write to memory address 42, it first applies the bitmask:

# address: 000000000000000000000000000000101010  (decimal 42)
# mask:    000000000000000000000000000000X1001X
# result:  000000000000000000000000000000X1101X
# After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)
# 000000000000000000000000000000111010  (decimal 58)
# 000000000000000000000000000000111011  (decimal 59)
# Next, the program is about to write to memory address 26 with a different bitmask:

# address: 000000000000000000000000000000011010  (decimal 26)
# mask:    00000000000000000000000000000000X0XX
# result:  00000000000000000000000000000001X0XX
# This results in an address with three floating bits, causing writes to eight memory addresses:

# 000000000000000000000000000000010000  (decimal 16)
# 000000000000000000000000000000010001  (decimal 17)
# 000000000000000000000000000000010010  (decimal 18)
# 000000000000000000000000000000010011  (decimal 19)
# 000000000000000000000000000000011000  (decimal 24)
# 000000000000000000000000000000011001  (decimal 25)
# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)
# The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

# Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?

import copy

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()
    return read_data

def splitData(data):
    dataLine = []
    for line in data:
        newLine = line.split(' = ')
        if newLine[0] != 'mask':
            newLine[0] = int(newLine[0].lstrip("mem[").rstrip("]"))
            newLine[0] = f'{int(newLine[0]):036b}'
        dataLine.append(newLine)
    return dataLine

def processData(data):
    global mask
    global mem
    for line in data:
        if line[0] == 'mask':
            mask = line[1]
        else:
            line[0] = updateBits(mask,line[0])
            addrs = calcFloatingBits(line[0])
            for addr in addrs:
                mem.update({addr: int(line[1])})

def updateBits(mask,address):
    mask = [bit for bit in mask]
    address = [bit for bit in address]
    for i in range(36):
        if mask[i] != '0':
            address[i] = mask[i]
    return ''.join(address)

def calcFloatingBits(inputFloats):
    allOutputAddr = []
    floatCnt = inputFloats.count('X')
    for i in range(2 ** floatCnt): # 2 ^ floatCnt = all possible values
        addrFloat = copy.deepcopy(inputFloats)
        address = f'{int(i):0{floatCnt}b}'
        address = [j for j in address]
        for j in address:
            addrFloat = addrFloat.replace('X',j,1)
        allOutputAddr.append(int(addrFloat,2))
    return allOutputAddr

#///////////////////////////////////////////////////
inputFile = 'day14-input.txt'

mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
mem = {}

if __name__ == "__main__":
    data = fileInput()
    data = splitData(data)
    processData(data)
    print(sum(list(mem.values())))