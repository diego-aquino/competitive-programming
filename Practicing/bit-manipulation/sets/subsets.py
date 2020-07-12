def main():
    n = int(input())

    for subset in range(1 << n):
        print(bin(subset)[2:])

    print((1 << n) - 1)

main()
