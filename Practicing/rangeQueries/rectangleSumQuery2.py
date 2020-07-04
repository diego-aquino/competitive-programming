def main():
    def getInputs():
        n, m = map(lambda x: int(x), input().split())

        rect = []
        for row in range(n):
            rect.append(list(map(lambda x: int(x), input().split())))

        points = []
        for i in range(2):
            points.append(tuple(map(lambda x: int(x), input().split())))

        return n, m, rect, points

    def calculateSums():
        sums = []

        for row in range(n):
            if row > 0:
                sums.append([sums[row - 1][0] + rect[row][0]])

                for column in range(1, m):
                    areaB = sums[row][column - 1]
                    areaC = sums[row - 1][column]
                    areaD = sums[row - 1][column - 1]

                    sums[row].append(areaB + areaC - areaD + rect[row][column])
            else:
                sums.append([rect[0][0]])

                for column in range(1, m):
                    sums[0].append(sums[row][column - 1] + rect[row][column])

        return sums

    def sumQuery(startPoint, endPoint):
        row1, column1 = startPoint
        row2, column2 = endPoint

        if row1 > 0 and column1 > 0:
            areaA = sums[row2][column2]
            areaB = sums[row2][column1 - 1]
            areaC = sums[row1 - 1][column2]
            areaD = sums[row1 - 1][column1 - 1]

            return areaA - areaB - areaC + areaD

        elif row1 == 0 and column1 > 0:
            return sums[row2][column2] - sums[row2][column1 - 1]

        elif row1 > 0 and column1 == 0:
            return sums[row2][column2] - sums[row1 - 1][column2]

        else: # row1 == 0 and column1 == 0
            return sums[row2][column2]

    n, m, rect, points = getInputs()
    sums = calculateSums()
    print(sumQuery(*points))

main()
