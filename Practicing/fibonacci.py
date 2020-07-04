computed = {}

def main():
    for i in range(int(input())):
        solve()

def solve():

    def fib(n):
        if n < 2:
            return n
        else:
            if str(n) in computed:
                return computed[str(n)]
            else:
                solution = fib(n - 1) + fib(n - 2)
                computed[str(n)] = solution

                return solution

    target = int(input())
    print(fib(target))

main()
