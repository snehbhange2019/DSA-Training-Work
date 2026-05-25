arr1 = [1, 2, 2, 2, 1]
arr2 = [2, 2]

ans = []

for i in range(len(arr1)):
    count = 0

    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            count = count + 1

    if count > 0 and arr1[i] not in ans:
        ans.append(arr1[i])

print(ans)