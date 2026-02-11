def brute(arr,k):
    k=k%(len(arr))
    temp=arr[0:k]
    for i in range(k,len(arr)):
        arr[i-k]=arr[i]
    for i in range(len(arr)-k,len(arr)):
        arr[i]=temp[i-(len(arr)-k)]
    return arr
arr=[1,2,3,4,5,6,7]    
print(brute(arr,3))
def optimal(arr1,k):
    k=k%(len(arr))
    arr1[:k]=arr1[:k][::-1]
    arr1[k:]=arr1[k:][::-1]
    arr1.reverse()
    return arr1
arr1=[1,2,3,4,5,6,7]
print(optimal(arr1,3))