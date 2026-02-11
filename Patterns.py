from typing import List


def pattern1(n):
    for i in range(n):
        print("* "*n)
#pattern1(5)
def printNtimes(n: int) -> None:
    print("Coding Ninjas", end="\n")
    if n > 1:
        printNtimes(n-1)
#printNtimes(4)
def printN(i,n):
    if i>n:
        return 
    print(i)
    printN(i+1,n)
#printN(1,5)
def printnto1(i,n):
    if i<1:
        return
    print(i)
    printnto1(i-1,n)
#printnto1(5,5)
def print2(i,n):
    if i<1:
        return
    print2(i-1,n)
    print(i)
#print2(4,4)
def print3(i,n):
    if i>n:
        return 
    print3(i+1,n)
    print(i)
#print3(1,5)
def sum1(i,sum):
    if i<1:
        print(sum)
        return 
    sum1(i-1,sum+i)
#sum1(5,0)
def sum2(n):
    if n==0:
        return 0
    else:
        return n+sum2(n-1)
#print(sum2(3))    
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
#print(fact(3))    
def reverseArray(n: int, nums: List[int]) -> List[int]:
    start = 0
    end = n - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums
#print(reverseArray(5,[2,3,1,5,4]))
def revArray(arr):
    def rev(i):
        n=len(num)
        if i>=n/2:
            return num
        num[i],num[n-i-1]=num[n-i-1],num[i]
        rev(i+1)
    rev(0)
    return arr
num=[5,3,4,2,7]
#print(revArray(num))
def is_pal(s):
    s=''.join(ch for ch in s.lower() if ch.isalnum())
    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
#print(is_pal('madm'))
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
#print(fibonacci(4))
def hashbrute(n,arr):
    count=0
    for i in range(0,len(arr)):
        if arr[i]==n:
            count+=1
    return count
arr=[3,1,4,2,3,2,5,2,8,0]
#print(hashbrute(1,arr))
def hash(n,arr):
    hasharr=[0]*13
    for i in range(0,len(arr)):
        hasharr[arr[i]]+=1
    return hasharr[n]
arr=[1,2,1,3,2]
#print(hash(12,arr))
def hashing(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq
arr = [1, 2, 1, 3, 2]
#print(hashing(arr))
def hashing(arr, max_val):
    hasharr = [0] * (max_val + 1)
    for x in arr:
        hasharr[x] += 1
    return hasharr
arr = [1, 2, 1, 3, 2]
hasharr = hashing(arr, 5)
#print(hasharr)
#print("freq of 2 =", hasharr[2])
def charhash(s,c):
    hash=[0]*26
    s = s.lower()
    c = c.lower()
    for ch in s:
        if 'a' <= ch <= 'z':
            hash[ord(ch) - ord('a')] += 1
    return hash[ord(c)-ord('a')]
s='sfvmbdvhqcgjhgeeswa'
c='p'
print(charhash(s,c))
from collections import defaultdict

class Solution:
    # Function to count frequency of each element in the array using defaultdict
    def Frequency(self, arr, n):
        # Create a defaultdict to store frequency of each element
        freq_map = defaultdict(int)

        # Traverse the array and count frequencies
        for i in range(n):
            freq_map[arr[i]] += 1

        # Traverse through the defaultdict and print frequencies
        for key, value in freq_map.items():
            print(key, value)

if __name__ == "__main__":
    # Input array
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)

    # Create Solution instance
    sol = Solution()

    # Call the function to count frequencies
    sol.Frequency(arr, n)
