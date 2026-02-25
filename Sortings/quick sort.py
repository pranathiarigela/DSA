def quick(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quicksort(arr,low,high):
    if low<high:
        pindex=quick(arr,low,high)
        quicksort(arr,low,pindex-1)
        quicksort(arr,pindex+1,high)
    return arr

arr=[2,4,1,3,6,5]
print(quicksort(arr,0,len(arr)-1))