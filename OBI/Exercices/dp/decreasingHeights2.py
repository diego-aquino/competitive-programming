def main():
    t = int(input())
    for i in range(t):
        solve()

def solve():
    n, m = map(lambda x: int(x), input().split())

    height = []
    for i in range(n):
        height.append(list(map(lambda x: int(x), input().split())))

    operations = []
    for i in range(n):
        operations.append([0] * m)

    for row in range(n):
        for column in range(m):
            if row == 0 and column == 0: continue

            if row == 0:
                operations[row][column] = operations[row][column - 1]

                if height[row][column] > height[row][column - 1] + 1:
                    operations[row][column] += height[row][column] - (height[row][column - 1] + 1)
                    height[row][column] = height[row][column - 1] + 1

                elif height[row][column] < height[row][column - 1] + 1:
                    distance = row + column
                    operations[row][column] += (height[row][column - 1] - (height[row][column] - 1)) * distance

            elif column == 0:
                operations[row][column] = operations[row - 1][column]

                if height[row][column] > height[row - 1][column] + 1:
                    operations[row][column] += height[row][column] - (height[row - 1][column] + 1)
                    height[row][column] = height[row - 1][column] + 1

                elif height[row][column] < height[row - 1][column] + 1:
                    distance = row + column
                    operations[row][column] += (height[row - 1][column] - (height[row][column] - 1)) * distance

            else:
                shifted = [False, False]

                # operations coming from left
                left = operations[row][column - 1]

                if height[row][column] > height[row][column - 1] + 1:
                    left += height[row][column] - (height[row][column - 1] + 1)

                elif height[row][column] < height[row][column - 1] + 1:
                    distance = row + column
                    left += (height[row][column - 1] - (height[row][column] - 1)) * distance
                    shifted[0] = True

                # operations coming from top
                top = operations[row - 1][column]

                if height[row][column] > height[row - 1][column] + 1:
                    top += height[row][column] - (height[row - 1][column] + 1)

                elif height[row][column] < height[row - 1][column] + 1:
                    distance = row + column
                    top += (height[row - 1][column] - (height[row][column] - 1)) * distance
                    shifted[1] = True

                if left < top:
                    operations[row][column] = left

                    if not shifted[0]:
                        height[row][column] = height[row][column - 1] + 1
                else:
                    operations[row][column] = top

                    if not shifted[1]:
                        height[row][column] = height[row - 1][column] + 1

    print(operations[-1][-1])

main()
