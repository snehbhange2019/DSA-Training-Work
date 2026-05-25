#sum of even and odds number


n=int(input("enter size: "))
print("enter list element: ")
arr=[]
even=0
odd=0
for i in range(n):
    ele=int(input("enter element: "))
    arr.append(ele)

for i in range (len(arr)):
    if arr[i]%2==0:
        even=even+arr[i]
    else:
        odd=odd+arr[i]
        print("even",even)
        print("odd",odd)
    