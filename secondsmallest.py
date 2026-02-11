def secondsmallest(arr):
    smallest=arr[0]
    ssmallest=float('inf')
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            ssmallest=smallest
            smallest=arr[i]
        elif arr[i]!=smallest and arr[i]<ssmallest:
            ssmallest=arr[i]
    return ssmallest
arr=[2,2,2,6,5,4,3]
print(secondsmallest(arr))