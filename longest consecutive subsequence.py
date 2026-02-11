def linearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return True
        
def brute(nums):
    longest=1
    for i in range(len(nums)):
        x=nums[i]
        cnt=1
        while linearSearch(nums,x+1)==True:
            x=x+1
            cnt=cnt+1
        longest=max(longest,cnt)
    return longest
nums=[100,4,200,1,3,2]
print(brute(nums))

def better(nums):
    nums.sort()
    longest,cntcur=1,0
    lastsmaller=float('-inf')
    for i in range(len(nums)):
        if nums[i]-1==lastsmaller:
            cntcur+=1
            lastsmaller=nums[i]
        elif nums[i]!=lastsmaller:
            cntcur=1
            lastsmaller=nums[i]
        longest=max(longest,cntcur)
    return longest
print(better(nums))    

def optimal(nums):
    n=len(nums)
    if n==0:
        return 0
    longest=1
    st=set()
    for i in range(n):
        st.add(nums[i])
    for it in st:
        if it-1 not in st:
            cnt=1
            x=it
            while x+1 in st:
                x+=1
                cnt+=1
            longest=max(longest,cnt)
    return longest
print(optimal(nums))