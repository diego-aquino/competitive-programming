from math import ceil

def main():
    t = int(input())
    for i in range(t):
        solve()

def solve():
    a, b = map(lambda x: int(x), input().split())

    high, low = max(a, b), min(a, b)

    total = (low // 3) * 2

    remainder1 = high - (total * 3 / 2)
    remainder2 = low % 3

    if remainder1 >= 2 and remainder2 == 1:
        remainder1 -= 2
        remainder2 -= 1

    if remainder1 > 0:
        remainder1 -= min(remainder1 // 2, ceil(total / 2))

    print(total)

main()
