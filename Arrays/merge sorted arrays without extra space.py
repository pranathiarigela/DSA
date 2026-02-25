def merge1(arr1,arr2):
    left,right,index=0,0,0
    n=len(arr1)
    m=len(arr2)
    arr3=[0]*(n+m)
    while left<n and right<m:
        if arr1[left]<=arr2[right]:
            arr3[index]=arr1[left]
            left+=1
        else:
            arr3[index]=arr2[right]
            right+=1
        index+=1
    while left<n:
        arr3[index]=arr1[left]
        left+=1
        index+=1
    while right<m:
        arr3[index]=arr2[right]
        right+=1
        index+=1
    for i in range(len(arr3)):
        if i<n:
            arr1[i]=arr3[i]
        else:
            arr2[i-n]=arr3[i]
    return arr1,arr2
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
print(merge1(arr1,arr2))

def merge2(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    left=n-1
    right=0
    while left>=0 and right<m:
        if arr1[left]>arr2[right]:
            arr1[left],arr2[right]=arr2[right],arr1[left]
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()
    return [arr1,arr2]
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
print(merge2(arr1,arr2))

def merge3(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    length=n+m
    gap=(length//2)+(length%2)
    while gap>0:
        left=0
        right=left+gap
        while right<length:
            if left<n and right>=n:
                if arr1[left]>arr2[right-n]:
                    arr1[left],arr2[right-n]=arr2[right-n],arr1[left]
            elif left>=n:
                if arr2[left-n]>arr2[right-n]:
                    arr2[left-n],arr2[right-n]=arr2[right-n],arr2[left-n]
            else:
                if arr1[left]>arr1[right]:
                    arr1[left],arr1[right]=arr1[right],arr1[left]
            left+=1
            right+=1
        if gap==1:
            break
        gap=(gap//2)+(gap%2)
    return arr1,arr2
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
print(merge3(arr1,arr2))