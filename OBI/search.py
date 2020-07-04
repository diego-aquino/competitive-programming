def search(element, sequence):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (high + low) // 2

        if element < sequence[mid]:
            high = mid - 1
        elif element > sequence[mid]:
            low = mid + 1
        else:
            # return True
            return mid

    # return False

def test():
    from random import randrange
    from deltaTime import startMeasuringTime, deltaTime

    def getNewList(n):
        newList = []
        for i in range(n):
            newList.append(randrange(1, n + 1))

        newList.sort()
        return newList

    totalTimeBinarySearch, totalTimeSearch = 0.0, 0.0

    n = 100000
    for i in range(100):
        newList = getNewList(n)
        number = randrange(1, n + 1)

        startMeasuringTime()
        found1 = search(number, newList)
        totalTimeBinarySearch += deltaTime()

        startMeasuringTime()
        found2 = number in newList
        totalTimeSearch += deltaTime()

        if found1 != found2:
            print("Error")
            break

    print("Binary search: {:.20f}".format(totalTimeBinarySearch))
    print("Built-in search: {:.20f}".format(totalTimeSearch))

test()

# <sequence> must be sorted in increasing order
