from collections import deque

def main():
    def createSumTree():
        def powerOfTwo(num):
            while num > 1:
                num /= 2

            return num == 1

        def nextPowerOfTwo(num):
            result = 1

            while result < num:
                result *= 2

            return result

        if powerOfTwo(n):
            tree = [0] * (2*n)
        else:
            tree = [0] * (2*nextPowerOfTwo(n))

        i = -1
        for j in range(2*n - 1, n - 1, -1):
            tree[j] = array[i]
            i -= 1

        # childs of tree[i] -> tree[2*i] and tree[2*i + 1]
        # parent of tree[i] -> tree[i//2]

        for i in range(2*n - 1, 1, -1):
            parent = i // 2

            tree[parent] += tree[i]

        return tree

    def sumQuery(a, b):
        def getRangeRepresentedBy(curr):
            if isAtBottom(curr):
                return curr, curr

            left = 2 * curr
            right = 2 * curr + 1

            while not isAtBottom(left):
                left = 2 * left
                right = 2 * right + 1

            return left, right

        def isAtBottom(index):
            return n <= index <= 2*n - 1

        a += n
        b += n

        total = 0

        indexesLeft = set(range(a, b + 1))

        root = 1
        toVisit = deque([root])

        while len(indexesLeft) > 0:
            curr = toVisit.popleft()

            leftmost, rightmost = getRangeRepresentedBy(curr)

            if (leftmost in indexesLeft) and (rightmost in indexesLeft):
                total += tree[curr]

                for index in range(leftmost, rightmost + 1):
                    indexesLeft.remove(index)

            else:
                if not isAtBottom(curr) and \
                    not (rightmost < min(indexesLeft) or leftmost > max(indexesLeft)):

                    leftChild, rightChild = 2 * curr, 2 * curr + 1
                    toVisit.extend([leftChild, rightChild])

        return total

    array = tuple(map(lambda x: int(x), input().split()))
    n = len(array)

    tree = createSumTree()

    a, b = map(lambda x: int(x) - 1, input().split())
    print(sumQuery(a, b))

    print(tree)

main()
