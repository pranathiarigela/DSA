def majorityElement(nums):
    n = len(nums)
    for i in range(n):
        cnt = 0 
        for j in range(n):
            if nums[j] == nums[i]:
                cnt += 1
        if cnt > (n // 2):
            return nums[i]
    return -1
nums=[2,2,1,1,1,2,2]
print(majorityElement(nums))

def majorityElement1(nums):
    n = len(nums)
    mp = {}
    for num in nums:
        if num in mp:
            mp[num] += 1
        else:
            mp[num] = 1
    for num, count in mp.items():
        if count > n // 2:
            return num
    return -1
nums=[2,2,1,1,1,2,2]
print(majorityElement1(nums))

def majorityElement2(nums):
    cnt=0
    for i in range(len(nums)):
        if cnt==0:
            cnt=1
            el=nums[i]
        elif nums[i]==el:
            cnt+=1
        else:
            cnt-=1
    cnt1=0
    for i in range(len(nums)):
        if nums[i]==el:
            cnt1+=1
    if cnt1>len(nums)//2:
        return el
    return -1
nums=[2,2,1,1,1,2,2]
print(majorityElement2(nums))