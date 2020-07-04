def main():
    numbers = getNumbers()
    numbers.sort()
    printFormatted(numbers)

def getNumbers():
    return list(map(lambda x: int(x), input().split("+")))

def printFormatted(numbers):
    print("+".join(
        list(map(lambda x: str(x), numbers))
    ))

main()
