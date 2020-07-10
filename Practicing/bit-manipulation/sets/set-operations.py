set1 = 0
for num in [2, 6, 3, 8]:
    set1 |= (1 << num)

set2 = 0
for num in [1, 4, 3, 0, 8]:
    set2 |= (1 << num)

print(f'set1: {bin(set1)}')
print(f'set2: {bin(set2)}')

intersection = set1 & set2
print(f'intersection: {bin(intersection)}')

union = set1 | set2
print(f'union: {bin(union)}')

difference = set1 & (~set2) # elements in set2 removed from set1
print(f'difference: {bin(difference)}')

# processing individual bits
for i in range(set1.bit_length() - 1, -1, -1):
    if set1 & (1 << i) == 0:
        print('0', end='')
    else:
        print('1', end='')
