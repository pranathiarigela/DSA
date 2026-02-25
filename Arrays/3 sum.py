def brute(nums):
    seen=set()
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=tuple(sorted([nums[i],nums[j],nums[k]]))
                    seen.add(temp)
    return [list(temp) for temp in seen]
nums=[-1,0,1,2,-1,-4]
print(brute(nums))

def better(arr):
    n=len(arr)
    ans = set()
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in hashset:
                triplet = tuple(sorted([arr[i], arr[j], third]))
                ans.add(triplet)
            hashset.add(arr[j])
    return [list(triplet) for triplet in ans]
arr=[-1,0,1,2,-1,-4]
print(better(arr))

def threeSum(arr):
    n=len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                ans.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return ans
arr = [-1, 0, 1, 2, -1, -4]
print(threeSum(arr))