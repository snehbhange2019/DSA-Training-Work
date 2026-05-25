import sys

class GetNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        data = int(input("Enter data: "))
        newNode = GetNode(data)

        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.right is not None:
                ptr = ptr.right
            ptr.right = newNode
            newNode.left = ptr

        print(data, "is added")

    def traverse(self):
        if self.head is None:
            print("List not present")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.right
            print("None")


# Main program
if __name__ == '__main__':
    obj = LinkedList()

    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()
        elif n == 2:
            obj.traverse()
        elif n == 0:
            sys.exit(0)
        else:
            print("Invalid choice")