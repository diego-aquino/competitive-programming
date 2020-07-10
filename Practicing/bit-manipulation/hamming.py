from math import inf

def main():
    n, string = getInputs()
    print(minHammingDistance(string, n))

def getInputs():
    n = int(input())

    string = []
    for i in range(n):
        string.append(int(input(), 2))

    return n, string

def minHammingDistance(string, n):
    minDistance = inf

    for i in range(n - 1):
        for j in range(i + 1, n):
            minDistance = min(minDistance, getDistance(string[i], string[j]))

    return minDistance

def getDistance(s1, s2):
    difference = s1 ^ s2
    return bin(difference).count('1')

main()
