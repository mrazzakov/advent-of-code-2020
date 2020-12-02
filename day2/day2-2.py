# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

# Given the same example list from above:

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

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
        correct_letter = pw_array[1][0]
        position_1 = int(pw_array[0].split('-')[0])-1 #index starts at 1
        position_2 = int(pw_array[0].split('-')[1])-1 #index starts at 1
        password = pw_array[2]
                
        #check if password letter is in the correct poisions
        pw_correct = checkPosition(password, correct_letter, position_1, position_2)
        if pw_correct:
            password_count = password_count+1
        
    print(password_count)

def checkPosition(password, letter, pos1, pos2):
    #if one is true and the other is not, then the password is correct
    if (password[pos1] == letter) != (password[pos2] == letter):
        return True
    else:
        return False

if __name__ == "__main__":
    data = fileInput()
    checkPass(data)