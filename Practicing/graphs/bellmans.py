# 5 9
# 1 2 4
# 1 3 2
# 2 3 3
# 2 4 2
# 2 5 3
# 3 2 1
# 3 4 3
# 3 5 5
# 5 4 -5

def main():
    adj = getAdj()
    print(adj)

def getAdj():
    n, m = [int(x) for x in input().split()]

    adj = []
    for i in range(n):
        adj.append([0] * n)

    for i in range(m):
        newEdge = [int(x) for x in input().split()]
        adj[newEdge[0] - 1][newEdge[1] - 1] = newEdge[2]

    return adj

main()


