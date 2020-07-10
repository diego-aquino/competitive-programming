x = 8

k = 2

# Modify kth bit to 1:
# y = x | (1 << k)

# Modify kth bit to 0:
# y = x & ~(1 << k)

# Invert kth bit:
# y = x ^ (1 << k)

# Set last 1 bit to 0:
y = x & (x - 1)

# Check if x is a power of two:
powerOfTwo = x & (x - 1) == 0

print(x)
print(bin(x))

print(y)
print(bin(y))
