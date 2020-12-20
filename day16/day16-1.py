# --- Day 16: Ticket Translation ---
# As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

# Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

# You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

# The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

# Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'
# Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

# Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

# For example, suppose you have the following notes:

# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

# Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

import copy

def fileInput():
    f = open(inputFile, 'r')
    with open(inputFile) as f:
        read_data = f.read().split('\n')
    f.close()
    return read_data

def splitData(data):
    dataRow = []
    newData = []
    for line in data:
        if line == '':
            newData.append(dataRow)
            dataRow = []
        else:
            dataRow.append(line)
    newData.append(dataRow)
    return newData

def orgRules(rulesData):
    newRules = []
    for rule in rulesData:
        rule = rule.split(': ')
        rule.pop(0) #dont need the rule name
        rule = rule[0].split(' ')
        rule.pop(1) #dont need the 'or'
        for idx,word in enumerate(rule):
            rule[idx] = word.split('-')
        newRules.extend(rule)
    for idx,newRule in enumerate(newRules):
        newRules[idx] = int(newRule[0]), int(newRule[1])
    return newRules

def orgTickets(ticketData):
    ticketLine = []
    newTicketData = []
    ticketData.pop(0)
    for idx,ticket in enumerate(ticketData):
        ticketLine = ticket.split(',')
        for idx,tick in enumerate(ticketLine):
            ticketLine[idx] = int(tick)
        newTicketData.append(ticketLine)
    return newTicketData

def invalidTickets(rules,tickets):
    newTickets = []
    invalidTickets = []
    for ticket in tickets:
        newTickets.extend(ticket)
    invalidTickets = copy.deepcopy(newTickets)
    # print(newTickets)
    for ticket in newTickets:
        for rule in rules:
            if rule[0] <= ticket <= rule[1]:
                # print(ticket)
                invalidTickets.remove(ticket)
                break
    return sum(invalidTickets)


#///////////////////////////////////////////////////
inputFile = 'day16-input.txt'

if __name__ == "__main__":
    data = fileInput()
    data = splitData(data)
    # print(data[0])
    data[0] = orgRules(data[0])   #Rules
    data[2] = orgTickets(data[2]) #Nearby Tickets
    invalidTickets = invalidTickets(data[0],data[2])
    print(invalidTickets)
