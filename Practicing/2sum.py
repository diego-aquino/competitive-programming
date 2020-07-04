def main():
    k = int(input())
    array = list(map(lambda x: int(x), input().split()))

    n = len(array)
    array.sort()

    left, right = 0, n - 1

    while left < right:
        total = array[left] + array[right]

        if total > k:
            right -= 1
        elif total < k:
            left += 1
        else:
            print(array[left], array[right])
            return

    print('Not possible')

main()
