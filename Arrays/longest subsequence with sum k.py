def brute(arr,k):
    length=0
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            s=0
            for x in range(i,j+1):
                s+=arr[x]
            if s==k:
                length=max(length,j-i+1)
    return length
arr=[1,2,3,1,1,1,1,4,2,3]
print(brute(arr,3))

def brute_prefix(arr, k):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            if prefix[j + 1] - prefix[i] == k:
                max_len = max(max_len, j - i + 1)
    return max_len
arr = [1, 2, 3, 1, 1, 1, 1, 1, 4, 2, 3]
k = 3
print(brute_prefix(arr, k))

def longest_subarray_with_sum_k(arr, k):
    pre_sum_map = {}
    total = 0
    max_len = 0 
    for i in range(len(arr)):
        total += arr[i]
        # Case 1: subarray from index 0 to i
        if total == k:
            max_len = max(max_len, i + 1)
        # Case 2: remove prefix sum
        rem = total - k
        if rem in pre_sum_map:
            length = i - pre_sum_map[rem]
            max_len = max(max_len, length)
        # Store first occurrence of prefix sum
        if total not in pre_sum_map:
            pre_sum_map[total] = i
    return max_len
arr = [1, 2, 3, 1, 1, 1, 1, 4, 2]
k = 3
print(longest_subarray_with_sum_k(arr, k))

def optimal(arr,k):
    left=0
    right=0
    sum=arr[0]
    maxlen=0
    n=len(arr)
    while right<n:
        while left<=right and sum>k:
            sum-=arr[left]
            left+=1
        if sum==k:
            maxlen=max(maxlen,right-left+1)
        right+=1
        if right<n:
            sum+=arr[right]
    return maxlen
arr = [1, 2, 3, 1, 1, 1, 1, 4, 2]
k = 3
print(optimal(arr,3))