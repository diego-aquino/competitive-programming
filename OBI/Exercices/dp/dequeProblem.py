# Working solution!

def main():
    n = int(input())
    seq = tuple(map(lambda x: int(x), input().split()))

    points = []
    for i in range(n - 1):
        points.append([0] * n)

    if n == 1:
        print(seq[0])
        return

    for i in range(n - 1):
        points[i][i + 1] = (
            max(seq[i], seq[i + 1]),
            min(seq[i], seq[i + 1])
        )

    for k in range(2, n):
        for i in range(n - k):
            currLeft = seq[i] + points[i + 1][i + k][1]
            currRight = seq[i + k] + points[i][i + k - 1][1]
            nextLeft = points[i + 1][i + k][0]
            nextRight = points[i][i + k - 1][0]

            if currLeft > currRight:
                points[i][i + k] = (currLeft, nextLeft)
            else:
                points[i][i + k] = (currRight, nextRight)

        points.pop()

    print(points[0][n - 1][0] - points[0][n - 1][1])

main()
