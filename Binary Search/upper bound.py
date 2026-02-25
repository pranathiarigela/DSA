def upperBound(arr,x):
    for i in range(len(arr)):
        if arr[i]>x:
            return i
    return len(arr)
arr=[3,5,8,15,19]
print(upperBound(arr,15))
#TC-O(n)
#SC-O(1)

def opt(arr,x):
    low,high=0,len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[3,5,8,15,19]
print(opt(arr,9))
#TC--O(log n)
#SC--O(1)