def brute(arr):
    repeating=-1
    missing=-1
    for i in range(1,len(arr)+1):
        cnt=0
        for j in range(len(arr)):
            if arr[j]==i:
                cnt+=1
        if cnt==2:
            repeating=i
        elif cnt==0:
            missing=i
        if repeating!=-1 and missing!=-1:
            break  
    return [repeating,missing]
arr=[3,2,4,6,1,1]
print(brute(arr))
#TC----O(N^2)
#SC----O(1)

def better(arr):
    n=len(arr)
    hash=[0]*(n+1)
    for i in range(n):
        hash[arr[i]]+=1
    repeating=-1
    missing=-1
    for i in range(1,n+1):
        if hash[i]==2:
            repeating=i
        elif hash[i]==0:
            missing=i
        if repeating!=-1 and missing!=-1:
            break
    return [repeating,missing]
arr=[3,2,4,6,1,1]
print(better(arr))     
#TC----O(2n)
#SC----O(n) 

def optimal(arr):
    n=len(arr)
    sn=(n*(n+1))//2
    s2n=(n*(n+1)*(2*n+1))//6
    s,s2=0,0
    for i in range(n):
        s+=arr[i]
        s2+=arr[i]*arr[i]
    val1=s-sn
    val2=s2-s2n
    val2=val2//val1
    repeating=(val1+val2)//2
    missing=repeating-val1
    return [repeating,missing]
arr=[3,4,6,5,6,1]
print(optimal(arr))
#TC----O(n)
#SC----O(1) 