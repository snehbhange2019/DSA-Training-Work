def binary_serach(n,arr,target):
    flag=False
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
            flag=True
            loc=mid
            break;
        elif target<arr[mid]:
            
