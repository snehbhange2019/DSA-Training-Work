import sys
class GetNode:
    def __init__(self):
        self.data = None
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def append(self):
        data = int(input("Enter data: "))
        newnode = GetNode()
        newnode.data = data
        if self.head is None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newnode
        print(data, "is added")

    def traverse(self):
        if self.head is None:
            print("Linked list not present")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.next
            print()

    def addAfter(self):
        data = int(input("Enter data to insert: "))
        key = int(input("Enter node after which to insert: "))

        newnode = GetNode()
        newnode.data = data

        if self.head is None:
            print("List is empty")
            return

        ptr = self.head
        while ptr is not None:
            if ptr.data == key:
                break
            ptr = ptr.next

        if ptr is None:
            print("Key not found")
        else:
            newnode.next = ptr.next
            ptr.next = newnode
            print(data, "is added after", key)


if __name__ == "__main__":
    obj = linkedlist()

    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add After")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()
        elif n == 2:
            obj.traverse()
        elif n == 3:
            obj.addAfter()
        elif n == 0:
            sys.exit(0)
        else:
            print("Invalid choice")