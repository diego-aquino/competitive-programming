set1 = 0
for num in [1, 5, 6, 7]:
    set1 |= (1 << num)

# iterating through all subsets of set1
for subset in range(1 << set1.bit_length()):
    print(bin(subset))

# iterating through all subsets with k elements of set1
k = 3
for subset in range(1 << set1.bit_length()):
    if subset.bit_length() == k:
        print(bin(subset))

