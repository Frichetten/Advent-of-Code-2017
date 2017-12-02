# Advent of Code 2017 - Day 2
chksum = 0
with open('input.txt','r') as f:
  for line in f:
    a = [int(x) for x in line.split("\t")]
    chksum = chksum + (max(a) - min(a))
print chksum
