def subarraySum(arr, k):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            total = 0
            for m in range(i, j + 1):
                total += arr[m]
            if total == k:
                count += 1
    return count
arr=[1,2,3]
k=3
print(subarraySum(arr,k))

def subarraySum1(arr, k):
    n = len(arr)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total == k:
                count += 1
    return count
arr=[1,2,3]
k=3
print(subarraySum1(arr,k))

def subarraySum2(arr, k):
    n = len(arr)
    prefixSumCount = {}
    prefixSum = 0
    count = 0
    prefixSumCount[0] = 1
    for i in range(n):
        prefixSum += arr[i]
        remove = prefixSum - k
        if remove in prefixSumCount:
            count += prefixSumCount[remove]
        prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1
    return count
arr=[1,2,3]
k=3
print(subarraySum2(arr,k))