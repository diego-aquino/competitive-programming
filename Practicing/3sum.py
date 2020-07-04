def main():
    k = int(input())
    array = list(map(lambda x: int(x), input().split()))

    n = len(array)
    array.sort()

    left = 0
    right = n - 1

    while left < right - 1:
        subtotal = array[left] + array[right]
        completion = find(k - subtotal, left + 1, right - 1, array)

        if subtotal + completion > k:
            right -= 1
        elif subtotal + completion < k:
            left += 1
        else:
            print(array[left], completion, array[right])
            return

    print('Not possible')

def find(value, low, high, array):
    mid = (low + high) // 2

    while low <= high:
        mid = (low + high) // 2

        if value < array[mid]:
            high = mid - 1
        elif value > array[mid]:
            low = mid + 1
        else:
            return array[mid]

    return array[mid]

main()
