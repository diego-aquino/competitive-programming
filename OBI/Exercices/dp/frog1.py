def main():
    n, height = getInputs()

    cost = [0] * n
    cost[1] = abs(height[0] - height[1])

    for i in range(2, n):
        cost[i] = min(
            cost[i - 1] + abs(height[i] - height[i - 1]),
            cost[i - 2] + abs(height[i] - height[i - 2])
        )

    print(cost[-1])

def getInputs():
    return int(input()), tuple(map(lambda x: int(x), input().split()))

main()
