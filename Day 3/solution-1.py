x = 0
y = 0
i = 1
dist = 2
target = 368078
while 1 == 1:
    for j in range(dist-1):
        i += 1
        x += 1
        print i, x, y
        if i == target:
            exit()
    for j in range(dist-1):
        i += 1
        y -= 1
        print i, x, y
        if i == target:
            exit()
    for j in range(dist):
        i += 1
        x -= 1
        print i, x, y
        if i == target:
            exit()
    for j in range(dist):
        i += 1
        y += 1
        print i,  x, y
        if i == target:
            exit()

    dist += 2
