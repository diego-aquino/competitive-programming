def main():
    k, n = map(lambda x: int(x), input().split())

    price = []
    for product in range(k):
        price.append(tuple(map(lambda x: int(x), input().split())))
    # price[product][day]

    total = []
    for i in range(1 << k):
        total.append([0] * n)
    # total[subset][day]

    for subset in range(1 << k):
        for product in range(k):
            if (subset & (1 << product)):
                total[subset][0] += price[product][0]

    for day in range(1, n):
        for subset in range(1, 1 << k):
            total[subset][day] = total[subset][day - 1]

            for product in range(k):
                if subset & (1 << product):
                    total[subset][day] = min(
                        total[subset][day],
                        total[subset ^ (1 << product)][day - 1] + price[product][day]
                    )

    print(total[(1 << k) - 1][n - 1])

main()

# 3 8
# 6 9 5 2 8 9 1 6
# 8 2 6 2 7 5 7 2
# 5 3 9 7 3 5 1 4

# output: 5
