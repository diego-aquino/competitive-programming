a = set("abracadabra") # unique letters in the string
b = set("alacazam") # unique letters in the string

print(a)
print(b)

print(a - b) # letters in a but not in b
print(a | b) # letters in a or b or both
print(a & b) # letters in both a and b
print(a ^ b) # letters in a or b but not both
