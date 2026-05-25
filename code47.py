def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if __name__ =='__main__' :
                    arr = [6,23,2,4,1,8,56,3]
                    bubblesort(arr)
                    print(*arr)
                    print(arr)

  