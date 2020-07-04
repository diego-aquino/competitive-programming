def sort(sequence):
    n = len(sequence)

    if n < 2:
        return sequence
    elif n == 2:
        if sequence[0] > sequence[1]:
            sequence[0], sequence[1] = sequence[1], sequence[0]
        return sequence
    else:
        return merge(sort(sequence[:n//2]), sort(sequence[n//2:]))

def merge(sequence1, sequence2):
    mergedSequence = []

    while len(sequence1) > 0 and len(sequence2) > 0:
        if sequence1[0] < sequence2[0]:
            mergedSequence.append(sequence1.pop(0))
        else:
            mergedSequence.append(sequence2.pop(0))

    mergedSequence.extend(sequence1)
    mergedSequence.extend(sequence2)

    return mergedSequence

def test():
    from random import randrange
    from deltaTime import startMeasuringTime, deltaTime

    def getNewList(n):
        newList = []
        for i in range(n):
            newList.append(randrange(1, n + 1))

        return newList

    totalTimeMergeSort, totalTimeSort = 0.0, 0.0

    n = 100000
    for i in range(100):
        newList = getNewList(n)

        startMeasuringTime()
        sortedList1 = sort(newList)
        totalTimeMergeSort += deltaTime()

        startMeasuringTime()
        sortedList2 = newList.sort()
        totalTimeSort += deltaTime()

    print("Merge sort: {:.20f}".format(totalTimeMergeSort))
    print("Built-in sort: {:.20f}".format(totalTimeSort))

test()
