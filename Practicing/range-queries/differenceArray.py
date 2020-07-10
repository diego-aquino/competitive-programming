def main():
    array = list(map(lambda x: int(x), input().split()))
    n = len(array)

    diff = [array[0]]
    for i in range(1, n):
        diff.append(array[i] - array[i - 1])

    t = int(input())
    for i in range(t):
        start, end, value = map(lambda x: int(x), input().split())

        diff[start] += value
        if end < n - 1:
            diff[end + 1] -= value

        index = int(input())
        print(sum(diff[:index + 1]))

main()
