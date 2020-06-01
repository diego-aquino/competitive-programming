def main():
    lines = int(input())

    x = 0
    for i in range(lines):
        if input().count("+") == 2:
            x += 1
        else:
            x -= 1

    print(x)

main()
