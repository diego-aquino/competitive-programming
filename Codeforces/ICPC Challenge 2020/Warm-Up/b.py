from os import path

def main():
    def ls(nodes, start):
        if len(nodes) == 0:
            return []
        elif len(nodes) == 1:
            return nodes
        elif len(nodes) == 2:
            a, b = nodes
            if adj[a][b] == 1 or adj[b][a] == 1:
                return nodes - b
            else:
                return nodes

        elif len(nodes) == 3:
            a, b, c = nodes

            return max(
                set(a) | ls(nodes - a),
                set(b) | ls(nodes - b),
                set(c) | ls(nodes - c)
            , key=(lambda x: len(x)))

        else:
            subnodes = node.copy()
            return 1 + ls(nodes)

    inputFile = open(path.dirname(path.abspath(__file__)) + "\\b\\b0.in", "r")
    outputFile = open(path.dirname(path.abspath(__file__)) + "\\b\\b0.text", "w")

    n, m = map(lambda x: int(x), inputFile.readline().split())

    adj = []
    for i in range(n):
        adj.append([0] * n)

    for i in range(m):
        a, b = map(lambda x: int(x), inputFile.readline().split())
        adj[a - 1][b - 1] = 1

    maxSetLength = 0
    maxSet = [0] * n

    for v in range(n):
        nodes = set([v])
        for dest in range(n):
            if adj[v][dest] == 0:
                nodes.add(dest)

        subset = ls(nodes, v)
        if len(subset) > maxSetLength:
            maxSetLength = len(subset)

            for i in range(n):
                maxSet[i] = 0

            for node in subset:
                maxSet[node] = 1

    print(maxSetLength)
    print(maxSet)

    inputFile.close()
    outputFile.close()

main()
