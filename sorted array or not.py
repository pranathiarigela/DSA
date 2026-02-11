def sortedOrNot(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    return True
arr=[1,2,3,5,4]
print(sortedOrNot(arr))