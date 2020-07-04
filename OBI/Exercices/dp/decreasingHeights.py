def main():
    t = int(input())
    for i in range(t):
        solve()

def solve():
    n, m = map(lambda x: int(x), input().split())

    grid, height, distanceShifted = [], [], []
    for i in range(n):
        row = list(map(lambda x: int(x), input().split()))
        grid.append(row)
        height.append(row.copy())
        distanceShifted.append([0] * m)

    distanceShifted[0][0] = 1

    operations = []
    for i in range(n):
        operations.append([0] * m)

    # solving
    for row in range(n):
        for column in range(m):
            if row == 0 and column == 0: continue

            if row == 0:
                shifted = False

                # going left
                left = operations[row][column - 1]

                if grid[row][column] > height[row][column - 1] + 1:
                    left += grid[row][column] - (height[row][column - 1] + 1)
                elif grid[row][column] < height[row][column - 1] + 1:
                    shifted = True
                    left += (height[row][column - 1] - grid[row][column] + 1) * distanceShifted[row][column - 1]

                # checking
                if not shifted:
                    height[row][column] = height[row][column - 1] + 1

                operations[row][column] = left
                distanceShifted[row][column] = distanceShifted[row][column - 1] + 1

            elif column == 0:
                shifted = False

                # going down
                up = operations[row - 1][column]

                if grid[row][column] > height[row - 1][column] + 1:
                    up += grid[row][column] - (height[row - 1][column] + 1)
                elif grid[row][column] < height[row - 1][column] + 1:
                    shifted = True
                    up += (height[row - 1][column] - grid[row][column] + 1) * distanceShifted[row - 1][column]

                # checking
                if not shifted:
                    height[row][column] = height[row - 1][column] + 1

                operations[row][column] = up
                distanceShifted[row][column] = distanceShifted[row - 1][column] + 1

            else:
                shifted = [False, False]

                # going down
                up = operations[row - 1][column]

                if grid[row][column] > height[row - 1][column] + 1:
                    up += grid[row][column] - (height[row - 1][column] + 1)
                elif grid[row][column] < height[row - 1][column] + 1:
                    shifted[0] = True
                    up += (height[row - 1][column] - grid[row][column] + 1) * distanceShifted[row - 1][column]

                # going left
                left = operations[row][column - 1]

                if grid[row][column] > height[row][column - 1] + 1:
                    left += grid[row][column] - (height[row][column - 1] + 1)
                elif grid[row][column] < height[row][column - 1] + 1:
                    shifted[1] = True
                    left += (height[row][column - 1] - grid[row][column] + 1) * distanceShifted[row][column - 1]

                # checking
                if up < left:
                    if not shifted[0]:
                        height[row][column] = height[row - 1][column] + 1

                    operations[row][column] = up
                    distanceShifted[row][column] = distanceShifted[row - 1][column] + 1
                else:
                    if not shifted[1]:
                        height[row][column] = height[row][column - 1] + 1

                    operations[row][column] = left
                    distanceShifted[row][column] = distanceShifted[row][column - 1] + 1

    print(operations[-1][-1])

main()
