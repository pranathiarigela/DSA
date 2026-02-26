def opt1(arr,x):
    def first(arr,x):
        first=-1
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                first=mid
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return first
    def last(arr,x):
        last=-1
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                last=mid
                low=mid+1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return last
    firstocc=first(arr,x)
    if firstocc==-1:
        return 0
    lastocc=last(arr,x)
    return lastocc-firstocc+1
arr=[2,4,6,8,8,8,11,13]
print(opt1(arr,11))