def main():
    n = int(input())

    print(
        "Possible paths in a {0}x{0} grid: {1}"
        .format(n, getNumberOfPossiblePaths(n))
    )

def getNumberOfPossiblePaths(n):
    """Calculates the number of possible paths from the upper-left corner to the
    lower-right corner visiting each square exactly once"""
    destination = (n - 1, n - 1)

    paths = [[(0, 0), (1, 0)]]

    while True:
        newPaths = getNewPaths(n, paths, destination)

        if newPaths:
            paths = newPaths
            print("Current path length: {}".format(len(paths[0])))
            print("Total paths computed: {}".format(count))
        else:
            break

    paths = filterPathsByDestination(paths, destination)

    return len(paths) * 2

def getNewPaths(n, paths, destination):
    newPaths = []

    for path in paths:
        newDestinations = [
            (path[-1][0] - 1, path[-1][1]), #  <- x
            (path[-1][0] + 1, path[-1][1]), #     x ->
            (path[-1][0], path[-1][1] - 1), #  <- y
            (path[-1][0], path[-1][1] + 1) #     y ->
        ]

        for newDestination in newDestinations:
            updateCount()

            if valid(newDestination, path, n, destination):
                newPaths.append(path + [newDestination])

    return newPaths

count = 0
def updateCount():
    global count
    count += 1

def valid(newDestination, path, n, destination):
    if not validPoint(newDestination, n):
        return False

    if newDestination == destination and len(path) < (n**2 - 1):
        return False

    if newDestination in path:
        return False

    if path[-1][0] == newDestination[0] - 1:
        pointForward = (newDestination[0] + 1, newDestination[1])
        isHorizontal = True
    elif path[-1][0] == newDestination[0] + 1:
        pointForward = (newDestination[0] - 1, newDestination[1])
        isHorizontal = True
    elif path[-1][1] == newDestination[1] - 1:
        pointForward = (newDestination[0], newDestination[1] + 1)
        isHorizontal = False
    elif path[-1][1] == newDestination[1] + 1:
        pointForward = (newDestination[0], newDestination[1] - 1)
        isHorizontal = False

    if validPoint(pointForward, n):
        if pointForward in path:
            if canTurnEitherLeftOrRight(newDestination, path, n, isHorizontal):
                return False
    else:
        if canTurnEitherLeftOrRight(newDestination, path, n, isHorizontal):
            return False

    return True

def validPoint(point, n):
    return (0 <= point[0] < n) and (0 <= point[1] < n)

def canTurnEitherLeftOrRight(newDestination, path, n, isHorizontal):
    if isHorizontal:
        upPoint = (newDestination[0], newDestination[1] - 1)
        downPoint = (newDestination[0], newDestination[1] + 1)

        if validPoint(upPoint, n) and validPoint(downPoint, n):
            if upPoint not in path and downPoint not in path:
                return True
    else:
        leftPoint = (newDestination[0] - 1, newDestination[1])
        rightPoint = (newDestination[0] + 1, newDestination[1])

        if validPoint(leftPoint, n) and validPoint(rightPoint, n):
            if leftPoint not in path and rightPoint not in path:
                return True

    return False

def filterPathsByDestination(paths, destination):
    filteredPaths = []

    for path in paths:
        if str(path[-1]) == str(destination):
            filteredPaths.append(path)

    return filteredPaths

main()
