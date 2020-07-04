def solve():
    n = int(inputFile.readline())

    left, right = {}, {}

    for i in range(n):
        a, x, b = inputFile.readline().split()
        left[f"({a}, {x})"] = x
        right[f"{x}, {b}"] = b

    sentence = ""

    value = "0"
    for i in range(n):
        char = left[value]
        sentence += char
        value = right[char]

    print(sentence, file=outputFile)

from os import path

inputFile = open(f"{path.dirname(path.abspath(__file__))}\\tests\\1\\in4", "r")
solFile = open(f"{path.dirname(path.abspath(__file__))}\\tests\\1\\out4", "r")

outputFile = open(f"{path.dirname(path.abspath(__file__))}\\output.txt", "w")

solve()

outputFile.close()
outputFile = open(f"{path.dirname(path.abspath(__file__))}\\output.txt", "r")

if solFile.read() == outputFile.read():
    print("Accepted")

inputFile.close()
solFile.close()
outputFile.close()
