def maxprofit(nums):
    mini=nums[0]
    maxprofit=0
    for i in range(1,len(nums)):
        cost=nums[i]-mini
        maxprofit=max(maxprofit,cost)
        mini=min(mini,nums[i])
    return maxprofit
nums=[7,1,5,3,6,4]
print(maxprofit(nums))