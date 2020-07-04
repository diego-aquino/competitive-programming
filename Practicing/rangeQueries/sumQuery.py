def main():
    def sumQuery(start, end):
        if start > 0:
            return sums[end] - sums[start - 1]
        else:
            return sums[end]

    array = list(map(lambda x: int(x), input().split()))

    sums = [array[0]]

    for i in range(1, len(array)):
        sums.append(sums[i - 1] + array[i])

    print(sumQuery(0, 0))

main()
