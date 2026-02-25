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


def fourSum(arr,target):
    n=len(arr)
    st=set() 
    for i in range(n):
        for j in range(i + 1, n):
            seen=set()  
            for k in range(j + 1, n):
                required=target-arr[i]-arr[j]-arr[k]
                if required in seen:
                    temp=tuple(sorted([arr[i],arr[j],arr[k],required]))
                    st.add(temp)
                seen.add(arr[k])
    return [list(quad) for quad in st]
arr=[1, 0, -1, 0, -2, 2]
target=0
print(fourSum(arr,target))


def fourSumOpt(arr,target):
    n=len(arr)
    arr.sort()
    ans=[]
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            left,right=j+1,n-1
            while left<right:
                total=arr[i]+arr[j]+arr[left]+arr[right]
                if total==target:
                    ans.append([arr[i],arr[j],arr[left],arr[right]])
                    while left<right and arr[left]==arr[left+1]:
                        left+=1
                    while left<right and arr[right]==arr[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<target:
                    left+=1
                else:
                    right-=1
    return ans
arr=[1,0,-1,0,-2,2]
target=0
print(fourSumOpt(arr, target))