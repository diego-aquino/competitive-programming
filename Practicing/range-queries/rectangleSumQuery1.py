def main():
    def sumQuery(startPoint, endPoint):
        total = 0

        for row in range(startPoint[0], endPoint[0] + 1):
            if startPoint[1] > 0:
                total += sums[row][endPoint[1]] - sums[row][startPoint[1] - 1]
            else:
                total += sums[row][endPoint[1]]

        return total

    n, m = map(lambda x: int(x), input().split())

    rect = []
    for row in range(n):
        rect.append(list(map(lambda x: int(x), input().split())))

    sums = []
    for row in range(n):
        sums.append([rect[row][0]])

        for column in range(1, m):
            sums[row].append(sums[row][column - 1] + rect[row][column])

    print(sumQuery((0, 1), (2, 3)))

main()
