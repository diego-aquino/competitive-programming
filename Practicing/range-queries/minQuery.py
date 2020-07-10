from math import inf

def main():
    seq = tuple(map(lambda x: int(x), input().split()))
    n = len(seq)

    mins = []
    for i in range(n):
        mins.append([inf] * n)

    # b - a + 1 -> power of two
    # 1 2 4 8...

    difference = 0
    while difference < n:
        for i in range(0, n - difference):
            a, b = i, i + difference

            mins[a][b] = min(seq[a], seq[b])

        difference = (difference + 1) * 2 - 1

    for row in mins:
        print(row)

main()

# 1 3 4 8 6 1 4 2
