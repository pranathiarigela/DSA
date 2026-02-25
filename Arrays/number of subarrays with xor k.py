def countSubarraysXOR(A,B):
    count=0
    for i in range(len(A)):
        xorVal=0
        for j in range(i,len(A)):
            xorVal^=A[j]
            if xorVal==B:
                count+=1
    return count
A=[4,2,2,6,4]
B=6
print(countSubarraysXOR(A,B))

def countSubarrays(A,k):
    freq={0: 1}
    prefixXor=0
    count=0
    for num in A:
        prefixXor^=num
        target=prefixXor^k
        if target in freq:
            count+=freq[target]
        freq[prefixXor]=freq.get(prefixXor,0)+1
    return count
A=[4,2,2,6,4]
k=6
print(countSubarrays(A,k))
