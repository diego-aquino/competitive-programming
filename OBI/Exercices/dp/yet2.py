from math import inf

def main():
    n = int(input())

    cards = tuple(map(lambda x: int(x), input().split()))
    tree = getMaxTree(cards, n)

    maxScore = 0
    step = 0

    for i in range(n):
        if step == 0:
            total = 0
            maxCard = -inf

            for j in range(i, n):
                total += cards[j]
                if cards[j] > maxCard:
                    maxCard = cards[j]

                if total - maxCard > maxScore:
                    maxScore = total - maxCard

            step = 1

        else:
            total -= cards[i - 1]
            if cards[i - 1] == maxCard:
                maxCard = maxQuery(i, n - 1, tree, n)

            if total - maxCard > maxScore:
                maxScore = total - maxCard

            for j in range(n - 1, i, -1):
                total -= cards[j]
                if cards[j] == maxCard:
                    maxCard = maxQuery(i, j - 1, tree, n)

                if total - maxCard > maxScore:
                    maxScore = total - maxCard

            step = 0

    print(maxScore)

def getMaxTree(array, n):
    tree = [-inf] * (2*n)

    for i in range(n):
        tree[i + n] = array[i]

    for i in range(2*n - 1, 1, -1):
        if tree[i] > tree[i//2]:
            tree[i//2] = tree[i]

    return tree

def maxQuery(a, b, tree, n):
    maxCard = -inf

    a += n
    b += n

    while a <= b:
        if a % 2 == 1:
            if tree[a] > maxCard:
                maxCard = tree[a]
            a += 1

        if b % 2 == 0:
            if tree[b] > maxCard:
                maxCard = tree[b]
            b -= 1

        a //= 2
        b //= 2

    return maxCard

main()
