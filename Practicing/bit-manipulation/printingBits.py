x = 43
for i in range(5, -1, -1):
    if x & (1 << i):
        print('1', end='')
    else:
        print('0', end='')
