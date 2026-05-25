#intersaction of two arrays:
arr = [-1, 2, -3, 4, 5, -6]
arr1 = []   
arr2 = []   
ans = []

for i in range(len(arr)):
    if arr[i] < 0:
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])

print("Negative Array:", arr1)
print("Positive Array:", arr2)

i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    ans.append(arr1[i])
    ans.append(arr2[j])
    i = i + 1
    j = j + 1
while j < len(arr2):
    ans.append(arr2[j])
    j = j + 1
while i < len(arr1):
    ans.append(arr1[i])
    i = i + 1

print("Final Array:", ans)