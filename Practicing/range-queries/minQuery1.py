from math import sqrt, inf

def main():
    array = tuple(map(lambda x: int(x), input().split()))
    n = len(array)

    mins = []
    for i in range(n):
        mins.append([-inf] * n)

    for a in range(n):
        for b in range(a, n):
            if powerOfTwo(b - a + 1):
                w = (b - a + 1) // 2

                mins[a][b] = min(
                    mins[a][a + w - 1],
                    mins[a + w][b]
                )

    for row in mins:
        print(row)

def powerOfTwo(num):
    while num > 1:
        num /= 2

    return num == 1

main()
