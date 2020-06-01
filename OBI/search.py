def search(element, sequence):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (high + low) // 2

        if element < sequence[mid]:
            high = mid - 1
        elif element > sequence[mid]:
            low = mid + 1
        else:
            return mid

# <sequence> must be sorted in increasing order
