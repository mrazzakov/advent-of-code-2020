# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?

def main():
    f = open('day1-input.txt', 'r')
    with open('day1-input.txt') as f:
        read_data = f.read().split('\n')
    f.close()

# Not efficient at all, but works :)
    for i in read_data:
        for j in read_data:
            for(k) in read_data:
                if int(i)+int(j)+int(k) == 2020:
                    print(int(i)*int(j)*int(k))
                    break

if __name__ == "__main__":
    main()