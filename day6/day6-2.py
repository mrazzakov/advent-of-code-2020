# --- Part Two ---
# As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

# Using the same example as above:

# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b
# This list represents answers from five groups:

# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

import string

inputFile = 'day6-input.txt'

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n\n')
    f.close()

    return read_data

def questionCounter(data):
    count = 0
    switcher = dict(zip(string.ascii_lowercase, range(0,26)))
    for group in data:
        group = group.split()
        groupCount = [0] * 26
        for person in group:
            for question in person:
                groupCount[switcher.get(question)] = groupCount[switcher.get(question)] + 1
        for questionCount in groupCount:
            if questionCount == len(group):
                count = count + 1
    return count
                


if __name__ == "__main__":
    data = fileInput()
    print(questionCounter(data))