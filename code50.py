#descending order selection sort.
def selectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        
        loc = i
        for j in range(i + 1, n):
            if arr[j] > arr[loc]:
                loc = j
        
        arr[i], arr[loc] = arr[loc], arr[i]

if __name__ == "__main__":
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    selectionSort(arr)
    print("Sorted array:", arr)