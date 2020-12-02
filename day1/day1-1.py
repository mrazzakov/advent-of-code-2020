def main():
    f = open('day1-input.txt', 'r')
    with open('day1-input.txt') as f:
        read_data = f.read().split('\n')
    f.close()

    for i in read_data:
        for j in read_data:
            if int(i)+int(j) == 2020:
                print(int(i)*int(j))
                break

if __name__ == "__main__":
    main()