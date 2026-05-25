class stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isfull(self):
        return self.top == self.CAPACITY - 1

    def isempty(self):
        return self.top == -1

    def push(self, ele):
        if self.isfull():
            print("Stack is full")
        else:
            self.stack.append(ele)
            self.top += 1

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            ele = self.stack.pop()
            self.top -= 1
            return ele


if __name__ == '__main__':
    obj = stacks()
    arr = [1, 2, 3, 4, 5]
    for i in range(len(arr)):
        obj.push(arr[i])

   
    rev = []
    for i in range(len(arr)):
        rev.append(obj.pop())

    print("Original:", arr)
    print("Reversed:", rev)