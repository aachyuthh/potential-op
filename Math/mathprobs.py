def totalMovesbyBishop(a,b):
    result = min(a-1,b-1)+min(a-1,8-b)+min(8-a,b-1)+min(8-a,8-b)
    return result
# print(totalMovesbyBishop(1,2)) 

def PrimeSum(A):
    if A==4:
        return 2,2
    isPrime = [True for i in range(A+1)]
    isPrime[0],isPrime[1] = False, False
    p=2
    while p**2 < A:
        if isPrime[p] == True:
            for i in range(2*p,A,p):
                isPrime[i] = False
        p+=1
    primes = []
    for i in range(A+1):
        if isPrime[i]: primes.append(i)

    for number in primes:
        number2 = A-number
        if number2 in primes:
            return number,number2
    return 0,0

print(PrimeSum(20))

def reverse(num):
    '''
        Important to check that the number doesnt't exceed the INT_MAX or INT_MIN in java
        In python int and long are dynamic concepts
        Also simply reversing the interger using [::-1] may result in trailing zeros
    '''
    if num<0:
        result = -1 * int( str(num)[::-1] )
    else:
        result =  int( str(num)[::-1] )
    if abs(result) > 2**31 -1:
        return 0
    return result
