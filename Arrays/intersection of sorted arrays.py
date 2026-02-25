def brute_intersection(arr1, arr2):
    res = []
    visited = [False] * len(arr2)

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and not visited[j]:
                res.append(arr1[i])
                visited[j] = True
                break

    return res

def better_intersection(arr1, arr2):
    freq = {}
    res = []

    for x in arr1:
        freq[x] = freq.get(x, 0) + 1

    for x in arr2:
        if x in freq and freq[x] > 0:
            res.append(x)
            freq[x] -= 1

    return res

def intersection_with_duplicates(arr1, arr2):
    i = j = 0
    res = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            res.append(arr1[i])
            i += 1
            j += 1

    return res

arr1 = [1,1,2,3,4,4,5]
arr2 = [2,3,4,4,5,6]
print(intersection_with_duplicates(arr1, arr2))
print(brute_intersection(arr1, arr2))
print(better_intersection(arr1, arr2))