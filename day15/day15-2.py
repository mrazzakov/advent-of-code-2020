# --- Part Two ---
# Impressed, the Elves issue you a challenge: determine the 30000000th number spoken. For example, given the same starting numbers as above:

# Given 0,3,6, the 30000000th number spoken is 175594.
# Given 1,3,2, the 30000000th number spoken is 2578.
# Given 2,1,3, the 30000000th number spoken is 3544142.
# Given 1,2,3, the 30000000th number spoken is 261214.
# Given 2,3,1, the 30000000th number spoken is 6895259.
# Given 3,2,1, the 30000000th number spoken is 18.
# Given 3,1,2, the 30000000th number spoken is 362.
# Given your starting numbers, what will be the 30000000th number spoken?

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split(',')
    f.close()
    return read_data

def dictTransform(data):
    turn_count = 0
    dict_data = {}
    for num in data:
        turn_count += 1 #turn starts on count 1, so do it before and add extra count at the end
        dict_data.update({int(num):[0,turn_count]})
        prev_num = num
    dict_data.update({int(prev_num):[turn_count]})
    return dict_data,turn_count

def memGameTurn(dict_data,prev_num,turn_count):
    # print('-----------')
    # print('#',turn_count,prev_num, '->',dict_data,end=" ")

    if dict_data.get(prev_num) is None:
        dict_data.update({prev_num:[turn_count]})
        prev_num = 0
    elif len(dict_data.get(prev_num)) == 1:
        dict_data.update({prev_num:[dict_data.get(prev_num)[0],turn_count]})
        prev_num = dict_data.get(prev_num)[1]-dict_data.get(prev_num)[0]
    else:
        dict_data.update({prev_num:[dict_data.get(prev_num)[1],turn_count]})
        prev_num = dict_data.get(prev_num)[1]-dict_data.get(prev_num)[0]
    return dict_data,prev_num

def memGame(data):
    turn_end = 30000000
    prev_num = 0 #first turn after data is always new number

    dict_data,turn_start = dictTransform(data)
    for i in range(turn_start+1,turn_end):
        dict_data,prev_num = memGameTurn(dict_data,prev_num,i)
    return prev_num

#///////////////////////////////////////////////////
inputFile = 'day15-input.txt'


if __name__ == "__main__":
    data = fileInput()
    print(memGame(data))

