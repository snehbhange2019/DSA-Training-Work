import sys
class GetNode:
    def __init__(self):
        self.data=None
        self.next=None

        class linkedlist:
            def __init__(self):
                self.hard=None

                def append(self):
                    data=int(input("enter data:"))
                    newnode=GetNode()
                    newnode.data=data
                    if self.head==None:
                        self.head=newnode
                    else:
                        ptr=self.head
                        while ptr.next!=None:
                            ptr=ptr.next
                            ptr.next=newnode
                            print(data,"is added")

                def traverse(self):
                    if self.head==None:
                        print("Linked list not present")
                    else:
                        ptr=self.head
                        while ptr!=None:
                            print(ptr.data," -> ",end="")
                            ptr=ptr.next

                if __name__ =='main__':
                    obj=linkedlist()
                    while True:
                        print("1.append")
                        print("2.traverse")
                        print("0.exit")
                    n=int (input("select any choice:"))
                    if n==1:
                        obj.append()
                    elif n==2:
                        obj.traverse()
                    elif n==0:
                        sys.exit(0)
