arr=[1,2,3,4,5,6,7,8]
loc=3
print(arr)
for i in range(loc+1,len(arr)):
    arr[i-1]=arr[i]
    arr.pop()
    
print("Updated array:", arr)

    