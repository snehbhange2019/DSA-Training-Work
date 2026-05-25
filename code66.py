arr = [1, 2, 3, 4, 5]
k = 2

print(arr)
for j in range(k):
    temp = arr[len(arr) - 1]      
    
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = temp                 

print(arr)