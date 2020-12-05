# --- Part Two ---
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

# byr valid:   2002
# byr invalid: 2003

# hgt valid:   60in
# hgt valid:   190cm
# hgt invalid: 190in
# hgt invalid: 190

# hcl valid:   #123abc
# hcl invalid: #123abz
# hcl invalid: 123abc

# ecl valid:   brn
# ecl invalid: wat

# pid valid:   000000001
# pid invalid: 0123456789
# Here are some invalid passports:

# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# Here are some valid passports:

# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?



#outputs an array split per line of input

import string



def fileInput():
    f = open('day4-input.txt', 'r')
    with open('day4-input.txt') as f:
        read_data = f.read().split('\n\n')
    f.close()

    return read_data

def splitFields(passport):
    for cred in passport:
        cred = cred.split(':')

def isHex(inString):
    hex_string = set(string.hexdigits)
    return all(c in hex_string for c in inString)

def checkFields(passport):
    byr = passport.get('byr')
    iyr = passport.get('iyr')
    eyr = passport.get('eyr')
    hgt = passport.get('hgt')
    hcl = passport.get('hcl')
    ecl = passport.get('ecl')
    pid = passport.get('pid')
    valid =  [False] * 7

    if 1920 <= int(byr) <= 2002:
        valid[0] = True

    if 2010 <= int(iyr) <= 2020:
        valid[1] = True

    if 2020 <= int(eyr) <= 2030:
        valid[2] = True

    if hgt.endswith('m'):
        hgt = hgt.rstrip('cm')
        if 150 <= int(hgt) <= 193:
            valid[3] = True
    if hgt.endswith('n'):
        hgt = hgt.rstrip('in')
        if 59 <= int(hgt) <= 76:
            valid[3] = True
    
    if hcl.startswith('#') and len(hcl) == 7:
        hcl = hcl.lstrip('#')
        valid[4] = isHex(hcl)
    
    if ecl in ['amb','blu','brn','gry','grn','hzl','oth']:
        valid[5] = True

    if pid.isnumeric() and len(pid) == 9:
        valid[6] = True

    return all(valid)


def isValidPassport(passport):
    if len(passport) == 8:
        return checkFields(passport)
    elif (len(passport) == 7) and not ('cid' in passport):
        return checkFields(passport)
    else:
        return False

def checkCreds(data):
    count = 0
    for passport in data:
        passport = passport.split()
        passport = dict(s.split(':') for s in passport)
        if isValidPassport(passport):
            count = count+1
    return count


if __name__ == "__main__":
 
    data = fileInput()
    print(checkCreds(data))