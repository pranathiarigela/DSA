def brute(arr3,arr4):
    res = []
    for i in arr3:
        if i not in res:
            res.append(i)
    for j in arr4:
        if j not in res:
            res.append(j)
    return res
arr3=[1,1,2,3,4,5]
arr4=[2,3,4,4,5,6]
print(brute(arr3,arr4))

def better(arr1,arr2):
    set1=set()
    for i in range(len(arr1)):
        set1.add(arr1[i])
    for j in range(len(arr2)):
        set1.add(arr2[j])
    arr=list(set1)
    return arr
arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5,6]
print(better(arr1,arr2))

def optimal(arr5,arr6):
    i=0
    j=0
    union=[]
    while(i<len(arr5) and j<len(arr6)):
        if len(union)==0 or arr5[i]<=arr6[j]:
            if arr5[i] not in union:
                union.append(arr5[i])
            i+=1
        else:
            if arr6[j] not in union:
                union.append(arr6[j])
            j+=1
    while j<len(arr6):
        if arr6[j] not in union:
            union.append(arr6[j])
        j+=1
    while i<len(arr5):
        if arr5[i] not in union:
            union.append(arr5[i])
        i+=1  
    return union

def optimal_fixed(arr5, arr6):
    i = j = 0
    union = []

    while i < len(arr5) and j < len(arr6):
        if arr5[i] < arr6[j]:
            if not union or union[-1] != arr5[i]:
                union.append(arr5[i])
            i += 1
        elif arr5[i] > arr6[j]:
            if not union or union[-1] != arr6[j]:
                union.append(arr6[j])
            j += 1
        else:
            if not union or union[-1] != arr5[i]:
                union.append(arr5[i])
            i += 1
            j += 1

    while i < len(arr5):
        if union[-1] != arr5[i]:
            union.append(arr5[i])
        i += 1

    while j < len(arr6):
        if union[-1] != arr6[j]:
            union.append(arr6[j])
        j += 1

    return union

arr5=[1,1,2,3,4,5]
arr6=[2,3,4,4,5,6]
print(optimal(arr5,arr6))
print(optimal_fixed(arr5,arr6))