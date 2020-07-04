class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, rootValue):
        self.root = Node(rootValue)

    def insert(self, value):
        parent = self.root

        while True:
            if value < parent.value:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = Node(value)
                    break
            else:
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = Node(value)
                    break

    def find(self, value):
        current = self.root

        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            elif value > current.value:
                if current.right:
                    current = current.right
                else:
                    return False
            else:
                return True

    def printInOrder(self, current=None):
        if current == None:
            current = self.root

        if current.left:
            self.printInOrder(current.left)

        print(current.value, end=" ")

        if current.right:
            self.printInOrder(current.right)

newTree = Tree(10)

newTree.insert(9)
newTree.insert(8)
newTree.insert(11)
newTree.insert(17)

newTree.printInOrder()
