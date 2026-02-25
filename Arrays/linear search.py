def linearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
arr=[1,2,8,2,3,1]
print(linearSearch(arr,3))