def brute(arr):
    arr.sort()
    return arr[-1]
def large(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest
arr=[3,1,4,7,2,9]
print(brute(arr))
print(large(arr))