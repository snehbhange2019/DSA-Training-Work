class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()


class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, ele):
        self.queue.append(ele)

    def delete(self):
        if not self.isEmpty():
            return self.queue.pop(0)

    def traverse(self):
        print(self.queue)

def reverse_queue(q):
    s = Stack()

    while not q.isEmpty():
        s.push(q.delete())

    while not s.isEmpty():
        q.insert(s.pop())

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

print("Original Queue:")
q.traverse()

reverse_queue(q)

print("Reversed Queue:")
q.traverse()