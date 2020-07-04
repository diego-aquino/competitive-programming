def main():
    x = int(input())
    array = tuple(map(lambda x: int(x), input().split()))
    n = len(array)

    left, right = 0, 0

    total = array[left]

    while left < n:
        while right < n - 1 and total + array[right + 1] <= x:
            total += array[right + 1]
            right += 1

        if total == x:
            break

        total -= array[left]
        left += 1

    if left > right:
        print('Not possible')
    else:
        print(f'{left} -> {right}')

main()
