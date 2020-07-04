from  collections import deque

def main():
    m = int(1e9 + 7)

    n, k = map(lambda x: int(x), input().split())
    limit = tuple(map(lambda x: int(x), input().split()))

    if n > 1:
        uses = deque([
            [1 for i in range(min(limit[0] + 1, k + 1))]
        ])

        for i in range(1, n - 1):
            maxAccumulated = min(
                k,
                limit[i] + len(uses[0]) - 1
            )

            uses.append([0] * (maxAccumulated + 1))

            for accumulated in range(len(uses[0])):
                for x in range(min(limit[i] + 1, k - accumulated + 1)):
                    uses[1][x + accumulated] += 1

            uses.popleft()

        waysToShare = 0

        for accumulated in range(len(uses[0])):
            candiesLeft = k - accumulated

            if candiesLeft <= limit[-1]:
                waysToShare = (waysToShare % m) + (uses[0][accumulated] % m)

        print(waysToShare % m)

    else:
        if k > limit[0]:
            print(0)
        else:
            print(1)

main()
