def main():
    array = list(map(lambda x: int(x), input().split()))

    nearestSmallerElement = [None]
    stack = [array[0]]

    for i in range(1, len(array)):
        while len(stack) > 0 and stack[-1] >= array[i]:
            stack.pop()

        if len(stack) == 0:
            nearestSmallerElement.append(None)
        else:
            nearestSmallerElement.append(stack[-1])

        stack.append(array[i])

    print(nearestSmallerElement)

main()
