
# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?

def fileInput():
    f = open('day2-input.txt', 'r')
    with open('day2-input.txt') as f:
        read_data = f.read().split('\n')
    f.close()

    return read_data

def checkPass(pw_data):
    password_count = 0

    # 2-8 f: ffffffnffs -> [2-8, f:, ffffffnffs]
    for pw_line in pw_data:
        pw_array = pw_line.split()
        letter = pw_array[1][0]
        letter_count = 0
        letter_min = int(pw_array[0].split('-')[0])
        letter_max = int(pw_array[0].split('-')[1])
                
        #count number of letter
        for i in pw_array[2]:
            if i == letter:
                letter_count = letter_count+1

        #check if amount is between min and max
        pw_correct = checkAmount(letter_count,letter_min,letter_max)
        if pw_correct:
            password_count = password_count+1
        
    print(password_count)


def checkAmount(count,minimum,maximum):
    if (count >= minimum) and (count <= maximum):
        return True
    else:
        return False

if __name__ == "__main__":
    data = fileInput()
    checkPass(data)