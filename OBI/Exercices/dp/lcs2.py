def main():
    s1, s2 = input(), input()
    n, m = len(s1), len(s2)

    dp, previous = [], []
    for i in range(n + 1):
        dp.append([0] * (m + 1))
        previous.append([0] * (m + 1))

    for row in range(1, n + 1):
        for column in range(1, m + 1):
            if s1[row - 1] == s2[column - 1]:
                dp[row][column] = 1 + dp[row - 1][column - 1]
                previous[row][column] = (row - 1, column - 1)
            else:
                dpUp = dp[row - 1][column]
                dpLeft = dp[row][column - 1]

                if dpUp > dpLeft:
                    dp[row][column] = dpUp
                    previous[row][column] = (row - 1, column)
                else:
                    dp[row][column] = dpLeft
                    previous[row][column] = (row, column - 1)

    lcs = ''
    curr = (n, m)

    while True:
        row, column = curr
        if previous[row][column] == 0: break

        if s1[row - 1] == s2[column - 1]:
            lcs = f'{s1[row - 1]}{lcs}'

        curr = previous[row][column]

    print(lcs)

main()
