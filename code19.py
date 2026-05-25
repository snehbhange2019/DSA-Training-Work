n=int(input("enter size: "))
print("enter list element: ")
arr=[]
even=0
odd=0
e1=0
o1=0
for i in range(n):
    ele=int(input("enter element: "))
    arr.append(ele)

for i in range (len(arr)):
    if arr[i]%2==0:
        even=even+arr[i]
        e1=e1+1
    else:
        odd=odd+arr[i]
        o1=o1+1
        print
    