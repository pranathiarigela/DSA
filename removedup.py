def remDupBrute(nums1):
    seen=set()
    index=0
    for num in nums1:
        if num not in seen:
            seen.add(num)
            nums1[index]=num
            index+=1
    return index,nums1

def removeDup(nums):
    if not nums:
        return 0,[]
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1,nums
nums1=[1,2,2,2,3,4,4,5,6]
print(remDupBrute(nums1))
nums=[1,1,2,2,3,3,3,4,5,6]
print(removeDup(nums))