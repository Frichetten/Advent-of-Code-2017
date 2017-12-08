# Can I get away with just checking the chains?

data = []
with open('input2.txt', 'r') as f:
    for line in f:
        data.append(line[:-1])

# Let's put this in a more accessible datastructure
weights = {}
for item in data:
    weights[item[:item.find(" ")]] = item[item.find("(")+1:item.find(")")]

guide = {}
for item in data:
    if '->' in item:
        a = item[item.find('->')+3:].split(",")
        b = []
        for thing in a:
            b.append(thing.lstrip(' '))
        guide[item[:item.find(" ")]] = b

for key in guide.keys():
    print key
    for item in guide[key]:
        print weights[item]
    print ""
