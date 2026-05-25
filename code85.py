class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        print(data, "added at beginning")

    def add_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newNode

        print(data, "added at end")

    def traverse(self):
        ptr = self.head
        while ptr:
            print(ptr.data, "->", end=" ")
            ptr = ptr.next
        print("None")

obj = LinkedList()
obj.add_begin(10)
obj.add_end(20)
obj.add_begin(5)
obj.traverse()