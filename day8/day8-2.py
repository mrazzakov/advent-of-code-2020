# --- Part Two ---
# After some careful analysis, you believe that exactly one instruction is corrupted.

# Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

# The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

# For example, consider the same program from above:

# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

# However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

# nop +0  | 1
# acc +1  | 2
# jmp +4  | 3
# acc +3  |
# jmp -3  |
# acc -99 |
# acc +1  | 4
# nop -4  | 5
# acc +6  | 6
# After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
import copy

accVal = 0
nopJmp = []
inputFile = 'day8-input.txt'

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()

    return read_data

#makes data in [instruction,count,index, writeNopJmp] form
def organizeData(data):
    dataList = []
    for idx, line in enumerate(data):
        line = line.split()
        line[1] = int(line[1])
        line.insert(2,idx)
        line.insert(3,False)
        dataList.append(line)
    return dataList

def readInstruction(line, inputData, accVal, nopJmp, writeNopJmp):
    data = copy.deepcopy(inputData) #so we dont override input data
    if line > (len(data)-1):  #end of file
        return [False,accVal]
    if (data[line][2] == (len(data)-1)) and writeNopJmp == False:
        return [True,accVal]
    if (data[line][3] == True):
        return [False,accVal]
    if data[line][0] == 'nop':
        if writeNopJmp:
            nopJmp.append(data[line])
        data[line][3] = True
        return readInstruction(line+1, data, accVal, nopJmp, writeNopJmp) #go to next line
    elif data[line][0] == 'acc':
        data[line][3] = True
        accVal += data[line][1]
        return readInstruction(line+1, data, accVal, nopJmp, writeNopJmp) #go to next line
    elif data[line][0] == 'jmp':
        if writeNopJmp:
            nopJmp.append(data[line])
        data[line][3] = True
        return readInstruction(data[line][2] + data[line][1], data, accVal, nopJmp, writeNopJmp) #jump to offset

def fixData(data, nopJmpList):
    for nopJmp in nopJmpList:
        nopJmp[3] = False
        if nopJmp[0] == 'nop':
            nopJmp[0] = 'jmp'
        else:
            nopJmp[0] = 'nop'
        idx = nopJmp[2]
        orgLine = data[idx] #original line
        data[idx] = nopJmp #switch line
        isTrue = readInstruction(0, data, accVal, nopJmp, False)
        if isTrue[0]:
            return data
        data[idx] = orgLine #return back to original data


if __name__ == "__main__":
    data = fileInput()
    orgData = organizeData(data)
    readInstruction(0 ,orgData, accVal, nopJmp, True)
    fixData(orgData, nopJmp)
    print(readInstruction(0 ,orgData, accVal, nopJmp, True)[1])
    