def brute(arr):
    cnt=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                cnt+=1
    return cnt
arr=[5,3,2,4,1]
print(brute(arr))
#TC---O(n^2)
#SC---O(1)

def merge(arr,low,mid,high):
    cnt=0
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            cnt+=(mid-left+1)
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return cnt
def mergesort(arr,low,high):
    cnt=0
    if low>=high:
        return cnt
    mid=(low+high)//2
    cnt+=mergesort(arr,low,mid)
    cnt+=mergesort(arr,mid+1,high)
    cnt+=merge(arr,low,mid,high)
    return cnt
def countInversions(arr):
    return mergesort(arr,0,len(arr)-1)
arr=[5,3,2,4,1]
print(countInversions(arr))
#TC---O(n logn)
#SC---O(n)