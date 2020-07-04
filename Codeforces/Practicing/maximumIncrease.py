def main():
    n, array = getInputs()

    maxLength = 1

    i = 0
    while i < n:
        currLength = 1

        for j in range(i + 1, n):
            if array[j] > array[j - 1]:
                currLength += 1
            else:
                i = j - 1
                break

        if currLength > maxLength:
            maxLength = currLength

        i += 1

    print(maxLength)

def getInputs():
    return int(input()), list(map(lambda x: int(x), input().split()))

main()
