# --- Part Two ---
# Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

# Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

# For example, suppose you have the following notes:

# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

# Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

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
    ruleNames = []
    for rule in rulesData:
        rule = rule.split(': ')
        ruleNames.append(rule[0]) #put rules in list
        rule.pop(0) #dont need the rule name
        rule = rule[0].split(' ')
        rule.pop(1) #dont need the 'or'
        for idx,word in enumerate(rule):
            rule[idx] = word.split('-')
        newRules.extend(rule)
    for idx,newRule in enumerate(newRules):
        newRules[idx] = int(newRule[0]), int(newRule[1])
    return newRules,ruleNames

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

def validTickets(rules,tickets):
    validickets = copy.deepcopy(tickets)
    # print(newTickets)
    for ticket in tickets:
        for value in ticket:
            remove = True
            for rule in rules:
                if rule[0] <= value <= rule[1]:
                    remove = False
            if remove:
                validickets.remove(ticket)
                break
    return validickets

def organizeByPosition(tickets):
    # [[3, 9, 18], [15, 1, 5], [5, 14, 9]]
    newArray = []
    for i in range(len(tickets[0])):
        newArray.append(mapPosition(tickets,i))
    return newArray
    

def mapPosition(tickets,position):
    return [ticket[position] for ticket in tickets]

def setRules(rules, ruleNames, tickets):
    newRulesList = []
    newRule = []
    for idx,rule in enumerate(rules):
        newRule.extend(rule)
        if idx % 2 == 1:
            newRulesList.append(newRule)
            newRule = []

    correctRule = []
    for idxR,rule in enumerate(newRulesList):
        correctRow = []
        for idxT,ticket in enumerate(tickets):
            isRule = True
            for val in ticket:
                if not ((rule[0] <= val <= rule[1]) or (rule[2] <= val <= rule[3])):
                    isRule = False
                    break
            if isRule:
                # print(ruleNames[idxR],': Row',idxT)
                correctRow.append(idxT)
            # print('CR',correctRow)
        correctRule.append(correctRow)
    return correctRule

def matchRules(ruleSet):
    moreRules = False
    for rule in ruleSet:
        if len(rule) is not 1:
            moreRules = True

    if moreRules:
        for rule in ruleSet:
            if len(rule) is 1:
                ruleSet = deleteRule(ruleSet,rule[0])
                return matchRules(ruleSet)
    else:
        return ruleSet

def deleteRule(ruleSet,delRule):
    for rule in ruleSet:
        if len(rule) != 1:
            rule = rule.remove(delRule)
    return ruleSet


#///////////////////////////////////////////////////
inputFile = 'day16-test.txt'

if __name__ == "__main__":
    data = fileInput()
    data = splitData(data)
    # print(data[0])
    data[0],ruleNames = orgRules(data[0])   #Rules
    data[2] = orgTickets(data[2]) #Nearby Tickets
    validTickets = validTickets(data[0],data[2])
    print(data[0])
    
    positionTickets = organizeByPosition(validTickets)
    print(positionTickets)
    print(ruleNames)
    correctRules = setRules(data[0],ruleNames,positionTickets)
    print(matchRules(correctRules))
    

