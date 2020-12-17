

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()
    return read_data

#///////////////////////////////////////////////////
inputFile = 'day15-test.txt'

if __name__ == "__main__":
    data = fileInput()
