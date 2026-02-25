def secondlargest(arr):
    largest=arr[0]
    slargest=-1
    for i in range(1,len(arr)):
        if arr[i]>largest:
            slargest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>slargest:
            slargest=arr[i]
    return slargest

arr=[7,6,8,3,1,10,10,10,9]
print(secondlargest(arr))