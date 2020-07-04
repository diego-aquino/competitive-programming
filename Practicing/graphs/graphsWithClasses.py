


# Not working!!!




class Node:
    def __init__(self, nodeId):
        self.id = nodeId
        self.connections = []

    def addConnection(self, node):
        self.connections.append(node)

class City:
    def __init__(self, numberOfNodes):
        self.nodes = []
        for i in range(numberOfNodes):
            self.nodes.append(Node(i + 1))

    def lengthOfLongestPathFrom(self, nodeIndex):
        paths = [
            {
                "previous": None,
                "current": self.nodes[nodeIndex],
                "length": 1
            }
        ]

        while True:
            i = 0
            while i < len(paths):
                newPathFound = False

                path = paths[i]

                for connection in path["current"].connections:
                    newPath = path.copy()

                    if connection != newPath["previous"]:
                        if newPath["previous"]:
                            if connection.id > newPath["previous"].id:
                                newPath["previous"] = newPath["current"]
                                newPath["current"] = connection
                            else:
                                i += 1
                                continue
                        else:
                            newPath["previous"] = newPath["current"]
                            newPath["current"] = connection
                    else:
                        i += 1
                        continue

                    newPath["length"] += 1
                    paths.append(newPath)
                    paths.pop(i)

                    newPathFound = True

                if not newPathFound:
                    break

        return paths[0]["length"]

def main():
    n, m = map(lambda x: int(x), input().split())

    city = City(n)

    # getting connections
    for i in range(m):
        a, b = map(lambda x: int(x), input().split())

        city.nodes[a - 1].addConnection(city.nodes[b - 1])
        city.nodes[b - 1].addConnection(city.nodes[a - 1])

    # paths
    message = ""
    for i in range(m):
        message += city.lengthOfLongestPathFrom(i)

    print(message[:-1])

main()
