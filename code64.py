arr = []

n = int(input("Enter size: "))

for i in range(n):
    arr.append(int(input("Enter no: ")))

key = int(input("Enter element to insert: "))

loc = int(input("Enter position (0 to n): "))

if loc < 0 or loc > n:
    print("Invalid position")
else:
    arr.append(0)
    for i in range(n, loc, -1):
        arr[i] = arr[i-1]
    arr[loc] = key

print("Updated array:", arr)