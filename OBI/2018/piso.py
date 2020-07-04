def main():
    l, c = int(input()), int(input())

    type1 = c
    type2 = (l - 1 + c - 1) * 2

    if l > 1:
        curr = c - 1
        for i in range((l - 1) * 2):
            type1 += curr

            if curr == c:
                curr -= 1
            else:
                curr += 1

    print(type1)
    print(type2)

main()
