def main():
    n, d, a = int(input()), int(input()), int(input())

    if d >= a:
        print(d - a)
    else:
        print(n - a + d)

main()
