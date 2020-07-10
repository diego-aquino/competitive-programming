# 1 3 4 8
# binarySet = int('100011010', 2)

binarySet = 0

for num in [1, 3, 4, 8]:
    binarySet |= (1 << num)

for num in [3, 5, 8]:
    print(binarySet & (1 << num) != 0)

print(f"'{bin(binarySet)[2:]}': {binarySet}")
print(f'bit_length: {binarySet.bit_length()}')
