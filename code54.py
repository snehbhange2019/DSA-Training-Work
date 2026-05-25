import sys
class stacks:
    def push(self):
        pass
    def pop(self):
        pass
    def traverse (self):
        pass
    def peek(self):
        pass
   
    if __name__ =='__main__':
         obj = stacks()
         while True:
            print("1. push")
            print("2. pop")
            print("3. peek")
            print("4. traverse")
            print("0. exit")
            ch=int(input("select any choice"))
            if ch==1:
                obj.push()
            elif ch==2:
                obj.pop()
            elif ch==3:
                obj.push()
            elif ch==4:  
                obj.peek()
            elif ch==0:
                sys.exit(0)


