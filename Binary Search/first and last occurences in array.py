def brute(arr,x):
    first,last=-1,-1
    for i in range(len(arr)):
        if arr[i]==x:
            if first==-1:
                first=i
            last=i
    return [first,last]
arr=[2,4,6,8,8,8,11,13]
print(brute(arr,8))
#TC---O(n)
#SC---O(1)

def lowerbound(arr,x):
    low,high=0,len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def upperbound(arr,x):
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

def opt(arr,x):
    lb=lowerbound(arr,x)
    if lb==len(arr) or arr[lb]!=x:
        return [-1,-1]
    return [lb,upperbound(arr,x)-1]
arr=[2,4,6,8,8,8,11,13]
print(opt(arr,8))
#TC---2*O(logn)
#SC---O(1)

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
        return [-1,-1]
    lastocc=last(arr,x)
    return [firstocc,lastocc]
arr=[2,4,6,8,8,8,11,13]
print(opt1(arr,81))