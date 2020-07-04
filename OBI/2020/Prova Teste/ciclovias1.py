from collections import deque

def main():
    n, adj = getInputs()

    for i in range(n):
        print(longestPath(i, n, adj), end="")

        if i < (n - 1):
            print(end=" ")

def longestPath(start, n, adj):
    paths = deque([[start]])
    lengths = deque([1])

    while True:
        path = paths.popleft()
        currLength = lengths.popleft()

        for dest in adj[path[-1]]:
            if len(path) == 2:
                if dest > path[0]:
                    paths.append([path[1], dest])
                    lengths.append(currLength + 1)
            else:
                paths.append([path[0], dest])
                lengths.append(currLength + 1)

        if len(paths) == 0:
            return currLength

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([])

    for i in range(m):
        a, b = map(lambda x: int(x), input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    return n, adj

main()
