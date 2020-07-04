# 8847: ⊏
# 8848: ⊐
# 8851: ⊓
# 8852: ⊔

def main():
    n, m, tiles = getInputs()

    count = [0] * (n + 1)
    count[1] = 1
    count[2] = 3

    for x in range(3, n + 1):
        count[x] = count[x - 1] + (count[x - 2] * 2)

    print(count)

def getInputs():
    n, m = map(lambda x: int(x), input().split())
    n, m = max(n, m), min(n, m)

    # t = int(input())
    # tiles = set()
    # for i in range(t):
    #     tiles.add(tuple(map(lambda x: int(x), input().split())))

    return n, m, set()

main()
