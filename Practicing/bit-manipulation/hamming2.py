# hamming distance -> bin(string1 ^ string2).count('1')
# contiguos substrings of b -> for i in range(len(b) - len(a))

# store calculated values

def main():
    def getDistance(s2):
        s2 = int(s2, 2)

        if s2 in calculated:
            return calculated[s2]

        else:
            distance = bin(s1 ^ s2).count('1')
            calculated[s2] = distance
            return distance

    a, b = input(), input()
    n, m = len(a), len(b)

    s1 = int(a, 2)
    calculated = {}

    totalDistace = 0
    for start in range(m - n, -1, -1):
        totalDistace += getDistance(b[start:start + n])

    print(totalDistace)

main()
