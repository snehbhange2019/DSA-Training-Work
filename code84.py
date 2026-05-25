class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newNode

        print(data, "added")

obj = LinkedList()
obj.add(10)
obj.add(20)
obj.add(30)