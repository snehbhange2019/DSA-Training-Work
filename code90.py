import sys
class bst:
    def __init__(self, key):
        self.leftchild = None
        self.data = key
        self.rightchild = None

    def insert(self, key):
        if key < self.data:
            if self.leftchild:
                self.leftchild.insert(key)
            else:
                self.leftchild = bst(key)

        elif key > self.data:
            if self.rightchild:
                self.rightchild.insert(key)
            else:
                self.rightchild = bst(key)

    def preorder(self):
        print(self.data, end=" -> ")
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.data, end=" -> ")
        if self.rightchild:
            self.rightchild.inorder()

    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.data, end=" -> ")


if __name__ == '__main__':
    arr = [36, 26, 21, 31, 11, 24, 41, 56, 51, 66]
    root = bst(arr[0])  
    for i in range(1, len(arr)):
        root.insert(arr[i])
    while True:
        print("\n1.Insert")
        print("2.Preorder")
        print("3.Inorder")
        print("4.Postorder")
        print("0.Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            data = int(input("Enter value: "))
            root.insert(data)

        elif n == 2:
            root.preorder()
            print()

        elif n == 3:
            root.inorder()
            print()

        elif n == 4:
            root.postorder()
            print()

        elif n == 0:
            sys.exit()

        else:
            print("Invalid choice!")