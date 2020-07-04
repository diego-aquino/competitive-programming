from collections import deque

infinity = 31

def main():
    n, values = getInputs()

    calculated = []
    for i in range(n):
        calculated.append(0)
    calculated[-1] = deque()

    score = [0] * n
    maxScore = 0

    def solve(start, end):
        total, highest = 0, -infinity

        for i in range(start, end + 1):
            if len(calculated[i]) >= end - i > 0:
                subTotal, subHighest = calculated[i][len(calculated[i]) - (end - i)]

                total += subTotal
                if subHighest > highest:
                    highest = subHighest

                break

            else:
                total += values[i]
                if values[i] > highest:
                    highest = values[i]

        return total, highest

    for i in range(n - 2, -1, -1):
        calculated[i] = deque()

        for j in range(i + 1, n):
            total, highest = solve(i, j)
            calculated[i].appendleft((total, highest))

            if total - highest > score[i]:
                score[i] = total - highest

                if score[i] > maxScore:
                    maxScore = score[i]

        calculated[i + 1] = 0

    print(maxScore)

def getInputs():
    n = int(input())
    values = tuple(map(lambda x: int(x), input().split()))

    return n, values

main()
