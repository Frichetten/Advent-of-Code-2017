banks = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5 ,1 ,2 ,15, 13, 5, 14]

history = []
cycles = 0

while banks not in history:
    cycles += 1
    history.append(banks[:])
    i = banks.index(max(banks))
    n = banks[i]
    banks[i] = 0
    while n != 0:
        i += 1
        if i == len(banks):
            i = 0
        banks[i] += 1
        n -= 1
    print cycles
