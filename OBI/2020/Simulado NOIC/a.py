# Not working...

infinity = 1000000000

def main():
    n, org = getInputs()

    time = [[infinity] * n, [infinity] * n]

    left = [set(range(n)), set(range(n))]

    connected = [[None] * n, [None] * n]

    while len(left[0]) > 0:
        for i in left[0]:
            for j in left[1]:
                if (org[i][0] <= org[j][0]) and (org[i][1] >= org[j][1]):
                    deltaTime = abs(org[i][0] - org[j][0]) + abs(org[i][1] - org[j][1])

                    if (deltaTime < time[i]) and (deltaTime < time[j]):


                    if i not in left:
                        connected[connected[i]] = None
                        left.add(connected[connected[i]])

                    if j not in left:
                        connected[connected[j]] = None
                        left.add(connected[connected[j]])

                    time[i] = deltaTime
                    connected[i] = j
                    left.remove(i)

                    time[j] = deltaTime
                    connected[j] = i
                    left.remove(j)

    while len(left) > 0:
        queue = []

        for i in left:
            if i < n:
                for j in left:
                    if j >= n:


    print(sum(time) // 2)

def getInputs():
    n = int(input())

    org = []
    for i in range(n * 2):
        org.append(tuple(map(lambda x: int(x), input().split())))

    return n, org

main()
