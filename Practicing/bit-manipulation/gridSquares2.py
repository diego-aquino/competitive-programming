from math import factorial

def main():
    def validSquare(row, column):
        rowAsNumber = grid[row]
        square = rowAsNumber & (1 << (n - column - 1))

        return square != 0

    n, grid = getInputs()

    count = 0

    for row1 in range(n):
        for row2 in range(row1 + 1, n):
            validColumns = 0

            for column in range(n):
                if validSquare(row1, column) and validSquare(row2, column):
                    validColumns += 1

            if validColumns > 1:
                count += factorial(validColumns) / (2 * factorial(validColumns - 2))

    print(int(count))

def getInputs():
    n = int(input())

    grid = []
    for i in range(n):
        grid.append(int(input(), 2))

    return n, grid

main()
