# --- Part Two ---
# It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

# Consider again your shiny gold bag and the rules from the above example:

# faded blue bags contain 0 other bags.
# dotted black bags contain 0 other bags.
# vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
# dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

# Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

# Here's another example:

# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# In this example, a single shiny gold bag must contain 126 other bags.

# How many individual bags are required inside your single shiny gold bag?

inputFile = 'day7-input.txt'
bagColor = 'shiny gold'
multiple = 1

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
def findBags(bagColor, bags, multiple):
    count = 0
    if not bags.get(bagColor):
        return multiple
    for bag in bags.get(bagColor):
        count = count +  multiple * findBags(bag, bags, bags.get(bagColor).get(bag))
    return count + multiple

if __name__ == "__main__":
    data = fileInput()
    orgBags = organizeBags(data)
    print(findBags(bagColor,orgBags,multiple)-1)