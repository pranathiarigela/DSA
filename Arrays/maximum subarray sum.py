def brute(nums):
    maxi=float('-inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum=0
            for k in range(i,j+1):
                sum+=nums[k]
            maxi=max(maxi,sum)
    return maxi

def better(nums):
    maxi=float('-inf')
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            maxi=max(maxi,sum)
    return maxi
    
def optimal(nums):
    sum=0
    maxi=float('-inf')
    for i in range(len(nums)):
        sum+=nums[i]
        if sum>maxi:
            maxi=sum
        if sum<0:
            sum=0
    return maxi     
nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(brute(nums))
print(better(nums))
print(optimal(nums))