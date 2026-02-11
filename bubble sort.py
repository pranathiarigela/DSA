def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
arr=[13,46,24,52,20,9]
print(bubblesort(arr))
def bubblesortopt(arr):
    swap=0
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swap=1
        if swap==1:
            break
    return arr
arr=[1,2,3,4,5,6,7,8]
print(bubblesortopt(arr))