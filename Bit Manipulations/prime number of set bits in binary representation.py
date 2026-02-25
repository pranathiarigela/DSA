def countPrimeSetBits(left,right):
    primes={2,3,5,7,11,13,17,19,23,29,31}
    count=0
    for i in range(left,right+1):
        if i.bit_count() in primes:
            count+=1
    return count
print(countPrimeSetBits(6,10))