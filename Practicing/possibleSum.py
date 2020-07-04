def main():
    t = int(input())

    for i in range(t):
        print(solve())

def solve():
    x, numbers = getInputs()

    if x == 0:
        return "Possible"

    sums = getSplitSums(numbers)

    if sumPossible(x, sums):
        return "Possible"
    else:
        return "Not possible"

def getInputs():
    return int(input()), list(map(lambda x: int(x), input().split()))

def getSplitSums(numbers):
    n = len(numbers)

    splitNumbers = [numbers[:n//2], numbers[n//2:]]

    sums = []
    for currentList in splitNumbers:
        currentSums = []

        for i in range(len(currentList)):
            for j in range(i, len(currentList)):
                newSum = sum(currentList[i:j + 1])

                if newSum not in currentSums:
                    currentSums.append(newSum)

        currentSums.sort()
        sums.append(currentSums)

    return sums

def sumPossible(x, sums):
    for sum1 in sums[0]:
        if (sum1 == x) or found(x - sum1, sums[1]):
            print("{} + {}".format(sum1, x - sum1))
            return True

    for sum2 in sums[1]:
        if sum2 == x:
            print(sum2)
            return True

def found(element, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2

        if element < array[mid]:
            high = mid - 1
        elif element > array[mid]:
            low = mid + 1
        else:
            return True

    return False

main()
