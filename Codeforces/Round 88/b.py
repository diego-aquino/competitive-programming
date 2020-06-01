def main():
    t = int(input())

    for case in getCases(t):
        print(smallestTotalPrice(case))

def getCases(t):
    cases = []
    for i in range(t):
        data = input().split()
        grid = []
        for j in range(int(data[0])):
            grid.append(input())

        cases.append((data, grid))

    return cases

def smallestTotalPrice(case):
    m, x, y = list(map(lambda x: int(x), case[0][1:]))
    grid = case[1]

    if x * 2 <= y:
        only1x1 = True
    else:
        only1x1 = False

    return getPaveCost(grid, only1x1, m, x, y)

def getPaveCost(grid, only1x1, m, x, y):
    cost = 0

    for row in grid:
        if only1x1:
            cost += row.count(".") * x
        else:
            row += "*"

            lineOfWhites = 0

            for i in range(m + 1):
                if row[i] == ".":
                    lineOfWhites += 1
                else:
                    double = lineOfWhites // 2
                    single = lineOfWhites % 2

                    cost += single * x + double * y
                    lineOfWhites = 0

    return cost

main()
