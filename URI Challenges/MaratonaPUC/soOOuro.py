n = 100000

b = n % 257
c = n % 193
d = (b**16)**(1 / 22) * b**(3/11) - b + 4

# quality = x**d + b * x**2 + c

print(d)
