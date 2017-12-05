# First, lets load a list with the values
data = []
with open('input2.txt','r') as f:
    for line in f:
        data.append(int(line[:-1]))

steps = 0
bounds = len(data)
i = 0
while i < bounds or i >= 0:
    try:
        n = data[i]
        if n >= 3:
            data[i] -= 1
        else:
            data[i] += 1
        i += n
        steps += 1
    except:
        print steps
        exit()

    
