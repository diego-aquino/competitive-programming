def main():
    n, m, grid = getInputs()

    message = ""
    for i in range(n):
        message += solve(n, m, grid, i) + " "

    print(message[:-1])

def getInputs():
    n, m = list(map(lambda x: int(x), input().split()))

    grid = []
    for i in range(n):
        grid.append([0] * n)

    for i in range(m):
        newRoad = list(map(lambda x: int(x), input().split()))
        grid[newRoad[0] - 1][newRoad[1] - 1] = 1
        grid[newRoad[1] - 1][newRoad[0] - 1] = 1

    return n, m, grid

def solve(n, m, grid, start):
    paths = [[start + 1]]

    while True:
        newPaths = getNewPaths(paths, grid, n)

        if newPaths:
            validPaths = []

            for path in newPaths:
                if valid(path):
                    validPaths.append(path)

            if validPaths:
                paths = validPaths
            else: break

        else: break

    return str(len(paths[0]))

def getNewPaths(paths, grid, n):
    newPaths = []

    for path in paths:
        for i in range(n):
            if grid[path[-1] - 1][i] == 1:
                newPaths.append(path + [i + 1])

    return newPaths

def valid(path):
    n = len(path)

    if n > 2:
        return path[-3] < path[-1]

    return True

main()
