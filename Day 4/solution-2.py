# First let's read in all the options
count = 0
with open('input.txt','r') as f:
  for line in f:
    words = line[:-1].split(" ")
    print words
    good = True
    for item in words:
      words2 = words[:]
      words2.remove(item) 
      for item2 in words2:
        if sorted(item) == sorted(item2):
          good = False
        print item, item2
    if good == True:
      count += 1

print count
