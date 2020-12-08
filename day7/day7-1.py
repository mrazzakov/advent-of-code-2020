# --- Day 7: Handy Haversacks ---
# You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

# In the above rules, the following options would be available to you:

# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

inputFile = 'day7-input.txt'
bagColor = 'shiny gold'
count = 0

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()

    return read_data

# bag: {innerbags[0]:count[0],...,innerBag[x]:count[x]}
# {dark orange: {'bright white': 3, 'muted yellow': 4}}
# {bright white: {'shiny gold': 1}}
def organizeBags(bags):
    bagRule = {}
    for rule in bags:
        count = 0
        bagKey = ''
        bagVal = {}
        
        rule = rule.split('contain ')
        for bag in rule:
            bag = bag.split(', ')
            for string in bag:
                string = string.replace(' bags','')
                string = string.replace(' bag','')
                string = string.rstrip(' .')
                if string[0].isdigit():
                    string = string.split(' ',1)
                    bagVal.update({string[1]:int(string[0])})
                if count == 0:
                    count = count + 1
                    bagKey = string

        bagRule.update({bagKey:bagVal})
    return bagRule


#{'light red': {'bright white': 1, 'muted yellow': 2}, 'dark orange': {'bright white': 3, 'muted yellow': 4}, 'bright white': {'shiny gold': 1}, 'muted yellow': {'shiny gold': 2, 'faded blue': 9}, 'shiny gold': {'dark olive': 1, 'vibrant plum': 2}, 'dark olive': {'faded blue': 3, 'dotted black': 4}, 'vibrant plum': {'faded blue': 5, 'dotted black': 6}, 'faded blue': {}, 'dotted black': {}}       
def findBags(bagColor, bags, count):
    # print(bagColor)
    for bag in bags.copy():
        # print(bag,':',bags.get(bag))
        # check that a key exists
        if bags.get(bag) is not None and bags.get(bag).get(bagColor):
            count = count + 1
            print(count)
            bags.pop(bag)
            count = findBags(bag,bags,count)
    return count
        # for innerBag in bags.get(bag):
        #     print(innerBag)
        # print(bags.get(bag).get(bagColor))
        # if it does, findBags with that bagColor
        # print(bags[bag])


    # innerBags = bags.values()
    # print(innerBags)
    # for bag in innerBags:
    #     if bag.get(bagColor):
    #         print(bagColor)

    
if __name__ == "__main__":
    data = fileInput()
    orgBags = organizeBags(data)
    print(orgBags)
    print(findBags(bagColor,orgBags,count))