def leader(n):
    ans=[]
    for i in range(len(n)):
        leader=True
        for j in range(i+1,len(n)):
            if n[j]>n[i]:
                leader=False
                break
        if leader==True:
            ans.append(n[i])
    return ans
n=[10,22,12,3,0,6]
print(leader(n))

def optimal(n1):
    ans=[]
    maxi=float('-inf')
    for i in range(len(n1)-1,-1,-1):
        if n1[i]>maxi:
            ans.append(n1[i])
        maxi=max(n1[i],maxi)
    return ans[::-1]
n1=[10,22,12,3,0,6]

print(optimal(n1))