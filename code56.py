class stacks:
    def __init__(self):
        self.stack = []
        self.top = -1

    def isempty(self):
        return self.top == -1

    def push(self, ele):
        self.stack.append(ele)
        self.top += 1
        print(ele, "is pushed")

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            ele = self.stack.pop()
            self.top -= 1
            return ele

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[self.top])

    def traverse(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


# Main program
if __name__ == '__main__':
    obj = stacks()

    obj.push(10)
    obj.push(20)
    obj.push(30)

    obj.traverse()

    print("Popped:", obj.pop())

    obj.peek()