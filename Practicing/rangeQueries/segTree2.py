from math import inf

n = 0

def main():
    array = tuple(map(lambda x: int(x), input().split()))
    global n
    n = len(array)

    tree = getMinSegTree(array)
    # tree = getSumSegTree(array)

    a, b = map(lambda x: int(x), input().split())
    print(getMinInRange(a, b, tree))

    # while True:
    #     index, num = map(lambda x: int(x), input().split())

    #     if index == -1: break

    #     update(index, num, tree)
    #     print(tree)

def getSumSegTree(array):
    tree = [0] * (2*n)
    for i in range(-1, - n - 1, -1):
        tree[i] = array[i]

    for i in range(2*n - 1, 1, -1):
        tree[i // 2] += tree[i]

    return tree

def getSum(a, b, tree):
    a += n
    b += n

    total = 0
    while a <= b:
        if a % 2 == 1:
            total += tree[a]
            a += 1
        if b % 2 == 0:
            total += tree[b]
            b -= 1

        a //= 2
        b //= 2

    return total

def update(index, value, tree):
    index += n

    tree[index] = value

    while index > 1:
        if index % 2 == 0:
            tree[index // 2] = tree[index] + tree[index + 1]
        else:
            tree[index // 2] = tree[index - 1] + tree[index]

        index //= 2

def getMinSegTree(array):
    # if powerOfTwo(n):
    #     tree = [0] * (2*n)
    # else:
    #     tree = [0] * (2*nextPowerOfTwo(n))
    tree = [inf] * (2*n)

    for i in range(-1, - n - 1, -1):
        tree[i] = array[i]

    for i in range(2*n - 1, 1, -1):
        tree[i // 2] = min(tree[i // 2], tree[i])

    return tree

def getMinInRange(a, b, tree):
    a += n
    b += n

    minNumber = inf

    while a <= b:
        if a % 2 == 1:
            minNumber = min(minNumber, tree[a])
            a += 1
        if b % 2 == 0:
            minNumber = min(minNumber, tree[b])
            b -= 1
        a //= 2
        b //= 2

    return minNumber

main()
