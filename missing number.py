def brute(arr):
    n=len(arr)
    for i in range(1,n+1):
        flag=0
        for j in range(n):
            if arr[j]==i:
                flag=1
                break
        if flag==0:
            return i
arr=[1,2,3,4,6]
print(brute(arr))

def hash(arr1):
    n=len(arr1)+1
    hash=[0]*(n+1)
    for i in range(n-1):
        hash[arr1[i]]+=1
    for i in range(1,n+1):
        if hash[i]==0:
            return i
    return -1
arr1=[1,2,3,4,6]
print(hash(arr1))

def optimal(arr2):
    n=len(arr2)+1
    tsum=sum(arr2)
    esum=(n*(n+1))//2
    return esum-tsum
arr2=[1,2,3,5]
print(optimal(arr2))

def xor(arr4):
    xor1,xor2=0,0
    n=len(arr4)+1
    for i in range(len(arr4)):
        xor2=xor2^arr4[i]
        xor1=xor1^(i+1)
    xor1=xor1^n
    return xor1^xor2
arr4=[1,3,4,5]
print(xor(arr4))