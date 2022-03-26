'''
Sieve of Eratosthenes - to find the prime numbers less than or equal to n(given n)
Time Complexity is O( n * log(log n) )
'''

def sieveofE(n):
    isPrime = [True for i in range(n+1)]
    isPrime[0], isPrime[1] = False,False
    p =2
    while p**2 < n:
        if isPrime[p] == True:
            for i in range(2*p,n,p):
                isPrime[i] = False
            
        p+=1
    
    for i in range(n+1):
        if isPrime[i]: print(i)

    pass
    
sieveofE(1)

'''
GCD of 2 numbers:
GCD(a,b) = GCD(a-b,b)
GCD(a,b) = GCD(b,a%b)
'''

def GCD(a,b):
    if a%b == 0: return b
    else:
        return GCD(b,a%b)

# print(GCD(60,18))

