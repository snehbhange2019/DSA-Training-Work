def linear_search(n,arr,target):
    flag=False
    for i in range(n):
        if target!=arr[i]:
            pass
        else:
            flag=True
            loc=i
            if flag==True:
             print("search is successful and present at",loc)
    else:
        print("search is unsuccessful")

if __name__ == '__main__':
    n=int(input("enter size: "))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        target=int(input("enter no which is to be search"))
        linear_search(n,arr,target)
        