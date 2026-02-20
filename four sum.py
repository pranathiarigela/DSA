def brute(nums):
    seen=set()
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l]==0:
                        temp=tuple(sorted([nums[i],nums[j],nums[k],nums[l]]))
                        seen.add(temp)
    return [list(temp) for temp in seen]
nums=[-1,0,0,1,2,-1,-4]
print(brute(nums))