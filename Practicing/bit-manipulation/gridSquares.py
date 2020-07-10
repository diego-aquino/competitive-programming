def main():
    def validSquare(row, column):
        square = grid[row] & (1 << (n - column - 1))
        return square != 0

    def validComplements(point1, point2):
        topRight = (point1[0], point2[1])
        bottomLeft = (point2[0], point1[1])

        return validSquare(*topRight) and validSquare(*bottomLeft)

    n, grid = getInputs()

    count = 0

    for row1 in range(n):
        for column1 in range(n):
            if not validSquare(row1, column1): continue

            topLeft = (row1, column1)

            for row2 in range(row1 + 1, n):
                for column2 in range(column1 + 1, n):
                    if not validSquare(row2, column2): continue

                    bottomRight = (row2, column2)
                    bottomRight = (row2, column2)

                    if validComplements(topLeft, bottomRight):
                        count += 1

    print(count)

def getInputs():
    n = int(input())

    grid = []
    for i in range(n):
        grid.append(int(input(), 2))

    return n, grid

main()
