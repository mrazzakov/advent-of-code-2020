# --- Day 8: Handheld Halting ---
# Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

# Their handheld game console won't turn on! They ask if you can take a look.

# You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

# The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

# acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
# For example, consider the following program:

# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# These instructions are visited in this order:

# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |
# First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

# This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

# Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

accVal = 0
inputFile = 'day8-input.txt'

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()

    return read_data

#makes data in [instruction,count,index] form
def organizeData(data):
    dataList = []
    for idx, line in enumerate(data):
        line = line.split()
        line[1] = int(line[1])
        line.insert(2,idx)
        line.insert(3,False)
        dataList.append(line)
    return dataList

def readInstruction(line, data, accVal):
    if data[line][3] == True:
        return accVal
    if data[line][0] == 'nop':
        data[line][3] = True
        return readInstruction(line+1, data, accVal)
    elif data[line][0] == 'acc':
        data[line][3] = True
        accVal += data[line][1]
        return readInstruction(line+1, data, accVal)
    elif data[line][0] == 'jmp':
        data[line][3] = True
        return readInstruction(data[line][2] + data[line][1], data, accVal)

if __name__ == "__main__":
    data = fileInput()
    orgData = organizeData(data)
    print(readInstruction(0,orgData, accVal))