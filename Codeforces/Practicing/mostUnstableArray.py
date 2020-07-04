def main():
    t = int(input())
    for i in range(t):
        solve()

def solve():
    n, total = map(lambda x: int(x), input().split())

    if n == 1:
        print(0)
    elif n == 2:
        print(total)
    else:
        print(total * 2)

main()
