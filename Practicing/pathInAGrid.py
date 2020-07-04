def main():
    n, grid = getInputs()

    sums = []
    for i in range(n):
        sums.append([0] * n)

    sums[0][0] = grid[0][0]

    previous = []
    for i in range(n):
        previous.append([None] * n)

    row = 0
    for column in range(1, n):
        sums[row][column] = sums[row][column - 1] + grid[row][column]
        previous[row][column] = (row, column - 1)

    column = 0
    for row in range(1, n):
        sums[row][column] = sums[row - 1][column] + grid[row][column]
        previous[row][column] = (row - 1, column)

    for row in range(1, n):
        for column in range(1, n):
            up = (sums[row - 1][column], (row - 1, column))
            left = (sums[row][column - 1], (row, column - 1))

            prev = max(up, left, key=byAccumulatedSum)

            sums[row][column] = prev[0] + grid[row][column]
            previous[row][column] = prev[1]

    print(f"\nGreatest sum: {sums[n - 1][n - 1]}")

    valueSequence = []
    pointSequence = set()
    curr = (n - 1, n - 1)

    while True:
        value = grid[curr[0]][curr[1]]

        valueSequence.append(value)
        pointSequence.add(curr)

        curr = previous[curr[0]][curr[1]]
        if curr == None: break

    valueSequence.reverse()
    print(f"Sequence: {' - '.join( map(lambda x: str(x), valueSequence))}")

    for row in range(n):
        line = ""

        for column in range(n):
            value = grid[row][column]

            if (row, column) in pointSequence:
                line += f"{value}* "
            else:
                line += f"{value}  "

        print(line)

def getInputs():
    n = int(input())

    grid = []
    for i in range(n):
        grid.append(
            list(map(lambda x: int(x), input().split()))
        )

    return n, grid

def byAccumulatedSum(x):
    return x[0]

main()
