def ncr(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res
print(ncr(4,2))

def row(n):
    ans=[]
    val=1
    ans.append(val)
    for i in range(1, n):
        val = val * (n - i)
        val = val // i
        ans.append(val)
    return ans
print(row(5))

def pascal(n):
    ans=[]
    for i in range(1,n+1):
        ans.append(row(i))
    return ans
print(pascal(5))