from collections import deque

from deltaTime import startMeasuringTime, deltaTime
from random import randrange

def main():
    # array = list(map(lambda x: int(x), input().split()))
    n = 50000

    array = []
    for i in range(n):
        array.append(randrange(0, n))

    windowLenght = randrange(1, n + 1)

    print(f'\narray: [{array[0]}, ... , {array[-1]}] (len: {n})')
    print(f'windowLenght: {windowLenght}\n')

    startMeasuringTime()
    result1 = solveStack(array, windowLenght)
    print(deltaTime())

    startMeasuringTime()
    result2 = solveNormal(array, windowLenght)
    print(deltaTime())

    assert result1 == result2

def solveStack(array, windowLenght):
    slidingWindowMin = []
    stack = deque()

    for i in range(len(array)):
        if len(stack) > 0 and stack[0][1] == i - windowLenght:
            stack.popleft()

        while len(stack) > 0 and stack[-1][0] >= array[i]:
            stack.pop()

        stack.append((array[i], i))

        if i >= windowLenght - 1:
            slidingWindowMin.append(stack[0][0])

    return slidingWindowMin

def solveNormal(array, windowLenght):
    slidingWindowMin = []

    stack = deque(array[:windowLenght])
    slidingWindowMin.append(min(stack))

    for i in range(windowLenght, len(array)):
        stack.popleft()
        stack.append(array[i])

        slidingWindowMin.append(min(stack))

    return slidingWindowMin

main()
