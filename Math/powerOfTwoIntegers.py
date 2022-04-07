'''
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 

'''
import math
def solve(A):
    #when the minimum power is exp, so maximum value of base is logA / log exp
    # the max value of base is sqrt(A) since the min value of exp is 2
    if A==1:
        return True
    for base in range(2,math.sqrt(A)):
        for exp in range(2, math.log(A)/math.log(exp)):
            if base**exp == A:
                return True

    return False

    #Time Complexity - O( sqrt(n) * log(n) )
