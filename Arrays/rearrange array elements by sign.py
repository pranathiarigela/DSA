def brute(nums):
    pos=[]
    neg=[]
    for i in range(len(nums)):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    for i in range(len(nums)//2):
        nums[2*i]=pos[i]
        nums[2*i+1]=neg[i]
    return nums
nums=[3,1,-2,-5,2,-4]
print(brute(nums))

def optimal(nums):
    n=len(nums)
    ans=[0]*n
    posIndex=0
    negIndex=1
    for i in range(n):
        if nums[i]<0:
            ans[negIndex]=nums[i]
            negIndex+=2
        else:
            ans[posIndex]=nums[i]
            posIndex+=2
    return ans
nums=[3,1,-2,-5,2,-4]
print(optimal(nums)) 

###if number of positives is not equal to number of negatives
def rearrange(nums):
    pos=[]
    neg=[]
    for i in range(len(nums)):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i]) 
    if len(pos)>len(neg):
        for i in range(len(neg)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        index=len(neg)*2
        for i in range(len(neg),len(pos)):
            nums[index]=pos[i]
            index+=1
    else:
        for i in range(len(pos)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i] 
        index=len(pos)*2
        for i in range(len(pos),len(neg)):
            nums[index]=neg[i]
            index+=1
    return nums
nums=[3,1,-2,9,-5,2,-4,6,7]
print(rearrange(nums)) 

##tc-O(2n) sc-O(n)