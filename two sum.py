##Only if array is sorted
def twoSum(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return [left,right]
        elif sum<target:
            left+=1
        else:
            right-=1
arr=[2,3,4]
print(twoSum(arr,6))

def twoSum2(arr,target):
    seen={}
    for i in range(len(arr)):
        needed=target-arr[i]
        if needed in seen:
            return [seen[needed],i]
        seen[arr[i]]=i
        
print(twoSum2(arr,6))

def two_sum_indices(arr, target):
    nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
    nums_with_index.sort(key=lambda x: x[0])
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        if current_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
arr = [2, 6, 5, 8, 11]
target = 14
print(two_sum_indices(arr,target))