def binarySearch(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[1,2,3,4,6,9,11]
print(binarySearch(arr,9))

def binarySearchRecursive(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binarySearchRecursive(arr,mid+1,high,target)
    else:
        return binarySearchRecursive(arr,low,mid-1,target)
arr=[2,3,4,5,6,8,9]
print(binarySearchRecursive(arr,0,len(arr)-1,8))