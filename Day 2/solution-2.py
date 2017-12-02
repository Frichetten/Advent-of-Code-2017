# Advent of Code 2017 - Day 2

def findNums(a):
  for one in a:
    for two in a:
      if ((one % two == 0) or (two % one == 0)) and one != two:
        big = max([one,two])
        small = min([one,two])
        return (big,small)

chksum = 0
with open('input.txt','r') as f:
  for line in f:
    a = [int(x) for x in line.split("\t")]
    b = findNums(a)
    chksum = chksum + (b[0] / b[1])
          
print chksum
