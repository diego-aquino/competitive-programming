solved = [0, 1]

def main():
    t = int(input())

    for i in range(t):
        solve()

def solve():
    n = int(input())
    print(fib(n))

    print(solved)

def fib(n):
    if n <= len(solved):
        return solved[n - 1]
    else:
        currNum, nextNum = solved[-2], solved[-1]

        for i in range(n - len(solved)):
            currNum, nextNum = nextNum, currNum + nextNum
            solved.append(nextNum)

        return solved[-1]

main()
