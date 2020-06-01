def main():
    n, s, connections = getInputs()
    print(getPingDiff(n, s, connections))

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    connections = []
    for i in range(n):
        connections.append([0] * n)

    for i in range(m):
        point = input().split()
        for j in range(3):
            point[j] = int(point[j])

        connections[point[0] - 1][point[1] - 1] = point[2]
        connections[point[1] - 1][point[0] - 1] = point[2]

    s = int(int(input()))

    return n, s, connections

def getPingDiff(n, s, connections):
    pings = [(str(s - 1), 0)]
    distance = 0

    while True:
        longestPath = pings[-1][0]
        if len(longestPath) == n:
            break

        newPings = []
        distance += 1

        for i in range(len(pings) - 1, -1, -1):
            path = pings[i][0]
            if len(path) == distance:
                for j in range(n):
                    lastIsland = int(pings[i][0][-1])

                    if connections[lastIsland][j] > 0 \
                        and not found(j, path):
                        newPings.append(
                            (pings[i][0] + str(j),
                            pings[i][1] + connections[lastIsland][j])
                        )
            else: break

        pings.extend(newPings)

    pings = sort(pings)
    optimalPings = getOptimalPings(n, s, pings)

    return optimalPings[-1][1] - optimalPings[0][1]

def sort(array):
    n = len(array)

    if n < 2:
        return array
    elif n == 2:
        if array[0][1] > array[1][1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        return merge(sort(array[:n//2]), sort(array[n//2:]))

def merge(array1, array2):
    mergedList = []

    while len(array1) > 0 and len(array2) > 0:
        if array1[0][1] < array2[0][1]:
            mergedList.append(array1.pop(0))
        else:
            mergedList.append(array2.pop(0))

    mergedList.extend(array1)
    mergedList.extend(array2)

    return mergedList

def found(element, array):
    for curr in array:
        if int(curr) == element:
            return True

    return False

def getOptimalPings(n, s, pings):
    optimalPings = []

    islandsLeft = list(range(n))
    islandsLeft.remove(s - 1)

    for ping in pings:
        finalNode = int(ping[0][-1])
        if finalNode != s - 1 and found(finalNode, islandsLeft):
            optimalPings.append(ping)
            islandsLeft.remove(finalNode)

        if len(islandsLeft) == 0:
            break

    return optimalPings

main()
