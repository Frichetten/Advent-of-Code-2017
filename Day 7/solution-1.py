# Can I get away with just checking the chains?

data = []
with open('input.txt', 'r') as f:
    for line in f:
        if '->' in line:
            data.append(line[:-1])

# Let's put this in a more accessible datastructure
guide = {}
for item in data:
    a = item[item.find('->')+3:].split(",")
    b = []
    for thing in a:
        b.append(thing.lstrip(' '))
    guide[item[:item.find(" ")]] = b

# We are trying to find someone who is a key, but not a value
hold = guide.keys()
for item in guide.keys():
    for key in guide.keys():
        if item in guide[key]:
            hold.remove(item)

print hold
