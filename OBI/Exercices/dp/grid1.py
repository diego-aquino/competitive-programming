def main():
    m = 1000000007

    h, w = map(lambda x: int(x), input().split())

    grid = []
    for row in range(h):
        grid.append(input())

    count = []
    for row in range(h):
        count.append([0] * w)

    for row in range(h):
        if grid[row][0] == "#":
            break
        count[row][0] = 1

    for column in range(w):
        if grid[0][column] == "#":
            break
        count[0][column] = 1

    for row in range(1, h):
        for column in range(1, w):
            if grid[row][column] == ".":
                count[row][column] = (
                    (count[row - 1][column] % m) +
                    (count[row][column - 1] % m)
                ) % m

    print(count[-1][-1])

main()
