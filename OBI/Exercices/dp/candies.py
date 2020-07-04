m = 1000000007

def main():
    n, k, limit = getInputs()

    left = {}
    for x in range(limit[0] + 1):
        num = k - x

        if num < 0: break
        else:
            if num in left:
                left[num] += 1
            else:
                left[num] = 1

    waysToShare = 0

    for i in range(1, n):
        newLeft = {}

        for prev in left:
            for x in range(limit[i] + 1):
                num = prev - x

                if i < n - 1: # i is not the last index
                    if num < 0: break

                    if num in newLeft:
                        newLeft[num] += 1
                    else:
                        newLeft[num] = 1

                else:
                    if num == 0:
                        waysToShare = (waysToShare + left[prev]) % m

                    elif num < 0: break

        left = newLeft

    print(waysToShare)

def getInputs():
    n, k = map(lambda x: int(x), input().split())
    limit = tuple(map(lambda x: int(x), input().split()))

    return n, k, limit

main()
