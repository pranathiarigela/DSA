from collections import defaultdict


def majorityElementTwo(nums):
    n = len(nums)
    result = [] 
    for i in range(n):
        if len(result) == 0 or result[0] != nums[i]:
            cnt = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    cnt += 1
            if cnt > (n // 3):
                result.append(nums[i])
        if len(result) == 2:
            break
    return result
nums=[1,1,1,3,3,2,2,2]
print(majorityElementTwo(nums))

def majorityElementTwo1(nums):
    n = len(nums)
    result = []
    mpp = defaultdict(int)
    mini = n // 3 + 1
    for num in nums:
        mpp[num] += 1
        if mpp[num] == mini:
            result.append(num)
        if len(result) == 2:
            break
    return result
nums=[1,1,1,3,3,2,2,2]
print(majorityElementTwo1(nums))

def majorityElementTwo2(nums):
    n = len(nums)
    cnt1, cnt2 = 0, 0
    el1, el2 = float('-inf'), float('-inf')
    for num in nums:
        if cnt1 == 0 and el2 != num:
            cnt1 = 1
            el1 = num 
        elif cnt2 == 0 and el1 != num:
            cnt2 = 1
            el2 = num 
        elif num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1 
        else:
            cnt1 -= 1 
            cnt2 -= 1
    cnt1, cnt2 = 0, 0 
    for num in nums:
        if num == el1:
            cnt1 += 1 
        if num == el2:
            cnt2 += 1
    mini = n // 3 + 1
    result = []
    if cnt1 >= mini:
        result.append(el1)
    if cnt2 >= mini and el1 != el2:
        result.append(el2)
    return result
nums=[1,1,1,3,3,2,2,2]
print(majorityElementTwo2(nums))