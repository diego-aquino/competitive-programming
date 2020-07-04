def main():
    t = int(input())
    for i in range(t):
        solve()

def solve():
    n, x, m = map(lambda x: int(x), input().split())
    operations = []
    for i in range(m):
        operations.append(list(map(lambda x: int(x), input().split())))

    total = 0

    initialRow = [0] * n
    initialRow[x] = 1

    for k in range(n):
        row = initialRow.copy()
        curr = x

        eligibleOps = getOps(curr, operations)

        for i in range(len(eligibleOps)):
            operation = eligibleOps[m]
            if operation[0] <= k and operation[1] >= curr:
                total += 1
                break

            elif i < (len(eligibleOps) - 1):
                nextOperation = operations[i + 1]

    print(total)

main()
