def maxSubArray(nums):
    maxi = float('-inf') 
    sum = 0 
    start = 0 
    ansStart = -1
    ansEnd = -1
    for i in range(len(nums)):
        if sum == 0:
            start = i
        sum += nums[i] 
        if sum > maxi:
            maxi = sum
            ansStart = start
            ansEnd = i
        if sum < 0:
            sum = 0
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(nums[i], end=" ")
    print("]")
    return maxi
nums = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
print(maxSubArray(nums))