#accept values from user find sum of list

n=int(input("enter size: "))
print("enter list element: ")
arr=[]
sum=0
for i in range(n):
    ele=int(input("enter element: "))
    arr.append(ele)

for i in range (len(arr)):
    sum=sum+arr[i]
        
