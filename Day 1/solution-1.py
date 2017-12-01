# Advent of Code 2017 - Day 1

# Let's start by making a list of the input.
hold = []
with open ('input.txt','r') as inp:
    for line in inp:
        for character in line:
            hold.append(character)

# If you have a newline you should pop it
if hold[-1] == "\n":
    hold.pop()

# Our strategy will be to go down the list and sum each 
# pair that we find. When we're done we will check the 
# ends of the list to make sure they dont match
sumval = 0
for i, val in enumerate(hold):
    if i == len(hold) - 1:
        if hold[-1] == hold[0]:
            sumval = sumval + int(val)
    elif val == hold[i+1]:
        sumval = sumval + int(val)

print sumval

# We got the right answer -> 1034
