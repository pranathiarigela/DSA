def brute(arr):
    temp=[]
    for i in range(len(arr)):
        if arr[i]!=0:
            temp.append(arr[i])
    n=len(temp)
    for i in range(len(temp)):
        arr[i]=temp[i]
    for i in range(n,len(arr)):
        arr[i]=0
    return arr
arr=[1,0,2,3,2,0,0,4,5,1]
print(brute(arr))
def optimal(arr1):
    j=-1
    for i in range(len(arr1)):
        if arr1[i]==0:
            j=i
            break
    for i in range(j+1,len(arr1)):
        if arr1[i]!=0:
            arr1[i],arr1[j]=arr1[j],arr1[i]
            j+=1
    return arr1
arr1=[1,0,2,3,2,0,0,4,5,1]
print(optimal(arr1))