class stacks:
    def __init__(self):
        self.stack = []
        self.top = -1

    def isempty(self):
        return self.top == -1

    def push(self, ele):
        self.stack.append(ele)
        self.top += 1

    def pop(self):
        if self.isempty():
            return None
        else:
            ele = self.stack.pop()
            self.top -= 1
            return ele


if __name__ == '__main__':
    obj = stacks()

    string = "Shreyanshi"

  
    for ch in string:
        obj.push(ch)

 
    rev = ""
    while not obj.isempty():
        rev += obj.pop()

    print("Original:", string)
    print("Reversed:", rev)
    