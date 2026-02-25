def maxProduct(nums):
    maxProd=nums[0]
    for i in range(len(nums)):
        prod=1
        for j in range(i,len(nums)):
            prod*=nums[j]
            maxProd = max(maxProd, prod)
    return maxProd
nums=[2,3,-2,4]
print(maxProduct(nums))
#TC---O(n^2)
#SC---O(1)


def maxProductSubArray(arr):
    n=len(arr)
    pre,suff=1,1
    ans=float('-inf')
    for i in range(n):
        if pre==0:
            pre=1
        if suff==0:
            suff=1
        pre*=arr[i]
        suff*=arr[n-i-1]
        ans=max(ans,pre,suff)
    return ans
arr=[2,3,-2,4]
print(maxProductSubArray(arr))
#TC--O(n)
#SC--O(1)

def maxProduct(nums):
    res=nums[0]
    maxProd=nums[0]
    minProd=nums[0]
    for i in range(1,len(nums)):
        curr=nums[i]
        if curr<0:
            maxProd,minProd=minProd,maxProd
        maxProd=max(curr,maxProd*curr)
        minProd=min(curr,minProd*curr)
        res=max(res,maxProd)
    return res
nums=[2,3,-2,4]
print(maxProduct(nums))
#TC---O(n)
#SC---O(1)