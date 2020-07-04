def main():
    n, k = map(lambda x: int(x), input().split())

    solved = 0
    timeLeft = 240 - k

    while solved < n:
        timeLeft -= 5 * (solved + 1)

        if timeLeft < 0:
            break
        else:
            solved += 1

    print(solved)

main()
