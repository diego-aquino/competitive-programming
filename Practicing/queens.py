def main():
    n = int(input())

    maxQueensCenarios = maxQueens(n)

    for cenario in maxQueensCenarios:
        for row in cenario:
            print(row)
        print()

    print(f"Total of cenarios: {len(maxQueensCenarios)}")

def maxQueens(n):
    cenarios = createInitialCenarios(n)

    for i in range(1, n): # For each row...
        numberOfOldCenarios = len(cenarios)
        for j in range(numberOfOldCenarios): # For each cenario...
            newCenarios = fillRow(cenarios[j], i, n)

            for newCenario in newCenarios:
                if validCenario(newCenario, i, n):
                    cenarios.append(newCenario)

        for j in range(numberOfOldCenarios):
            cenarios.pop(0)

    return cenarios

def createInitialCenarios(n):
    cenarios = []

    for i in range(n):
        currentCenario = []

        row = [0] * n
        currentCenario.append(row[:i] + [1] + row[i + 1:])

        for i in range(n - 1):
            currentCenario.append([0] * n)

        cenarios.append(currentCenario)

    return cenarios

def fillRow(cenario, row, n):
    newCenarios = []

    for i in range(n):
        newCenario = []
        for j in range(row):
            newCenario.append(cenario[j])

        newCenario.append(cenario[row][:i] + [1] + cenario[row][i + 1:])

        for j in range(row + 1, len(cenario)):
            newCenario.append(cenario[j])

        newCenarios.append(newCenario)

    return newCenarios

def validCenario(cenario, lastRow, n):
    for column in range(n):
        if cenario[lastRow][column] == 1:
            for row in range(n):
                if row != lastRow and cenario[row][column] == 1:
                    return False

            for vertical in [-1, 1]:
                for horizontal in [-1, 1]:
                    distance = 0

                    while True:
                        distance += 1

                        try:
                            x = lastRow + (horizontal * distance)
                            y = column + (vertical * distance)

                            if x >= 0 and y >= 0:
                                if cenario[x][y] == 1:
                                    return False
                            else: break

                        except: break
            break

    return True

main()
