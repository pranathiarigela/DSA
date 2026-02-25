def find_floor(arr,x):
    low,high=0,len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            ans=arr[mid]  
            low=mid+1
        else:
            high=mid-1
    return ans

def find_ceil(arr,x):
    low,high=0,len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=arr[mid] 
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[3,4,4,7,8,10]
x=5
print(find_floor(arr,x))
print(find_ceil(arr,x))

#TC---O(logn)
#SC---O(1)