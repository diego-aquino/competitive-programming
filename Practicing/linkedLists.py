class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

        if self.head:
            self.lenght = 1
        else:
            self.lenght = 0

    def insertAtHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.lenght += 1

    def insertAtTail(self, data):
        newNode = Node(data)
        lastNode = self.getLastNode()

        lastNode.next = newNode
        self.lenght += 1

    def getLastNode(self):
        current = self.head

        while current.next:
            current = current.next

        return current

    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            else:
                current = current.next

        return False

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                current.data = current.next.data
                current.next = current.next.next
                break
            else:
                current = current.next

    def __str__(self):
        completeList = "| "

        current = self.head
        while True:
            completeList += "{} -> ".format(current.data)

            if current.next:
                current = current.next
            else: break

        return completeList[:-3] + "|"

list1 = LinkedList()

for num in range(10, -1, -1):
    list1.insertAtHead(num)

print(list1)
