def main():
    infinity = 1e10

    n, k, height = getInputs()

    cost = [infinity] * n
    cost[0] = 0
    cost[1] = abs(height[0] - height[1])

    for i in range(2, n):
        for j in range(i - 1, i - k - 1, -1):
            if j >= 0:
                cost[i] = min(cost[i], cost[j] + abs(height[i] - height[j]))

    print(cost[-1])

def getInputs():
    n, k = map(lambda x: int(x), input().split())
    height = tuple(map(lambda x: int(x), input().split()))

    return n, k, height

main()
