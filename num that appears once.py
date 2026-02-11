def brute(arr):
    for i in range(len(arr)):
        num=arr[i]
        count=0
        for j in range(len(arr)):
            if arr[j]==num:
                count+=1
        if count==1:
            return num
arr=[1,1,2,3,3,4,4]
print(brute(arr))

def better(arr1):
    hash=[0]*(max(arr1)+1)
    for i in range(len(arr1)):
        hash[arr1[i]]+=1
    for i in range(len(arr1)):
        if hash[arr1[i]]==1:
            return arr1[i]
arr1=[1,1,2,2,3,4,4]
print(better(arr1))

def optimal(arr2):
    xorr=0
    for i in range(len(arr2)):
        xorr=xorr^arr2[i]
    return xorr
arr2=[1,1,3,3,6,6,9]
print(optimal(arr2))